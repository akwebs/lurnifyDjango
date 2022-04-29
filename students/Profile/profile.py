from all_imports.all_imports import *



def token_api(mobile):
    url = 'https://lurnify.in/api/token/'
    payload =  {
            'phone': mobile, 
            'password': mobile, 
           }    
    r = requests.post(url=url, data=payload)
   
    response=json.loads(r.text)
    
    token=response['access']
    
    
    return token
    

# Need to do logic
def check_course(course_id):
    get_course=course.objects.filter(id=course_id).first()
    if get_course.course_type == '2_year' :
        get_fee = int(get_course.course_fee) // 2
    else:
        get_fee= get_course.course_fee
    return get_fee

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication]) 
def registration_completed(request):
        get_obj = student_profile.objects.get(user=request.user)
        phone = get_obj.phone
        get_data=json.loads(request.body)
        
        if get_obj.email:
            email = get_obj.email
        else:
            email = ''
        if get_obj.address:
            address = get_obj.address
        else:
            address = ''
        if get_obj.city:
            city = get_obj.city
        else:
            city = ''
        if get_obj.state:
            state = get_obj.state
        else:
            state = ''
        if get_obj.date_of_birth:
            dob = get_obj.date_of_birth
        else:
            dob = ''

        if get_obj.pin_code:
            pin_code = get_obj.pin_code
        else:
            pin_code = ''

        if get_obj.coaching_name:
            coaching_name = get_obj.coaching_name
        else:
            coaching_name = ''

        if get_obj.coaching_city:
            coaching_city = get_obj.coaching_city
        else:
            coaching_city = ''

        if get_obj.course_program:
            course_program = get_obj.course_program
        else:
            course_program = ''            
 
        
        try:
            first_monday        =   get_data['firstMonday']
            course_date_id      =   get_data['course_dates_id']
            target              =   get_data['target_rank']
            daily_hours         =   get_data['daily_hours']
            get_obj.firstMonday=first_monday
            get_obj.save()            
            get_course_dates = course_dates.objects.filter(id=course_date_id).first()
            
            academic_details.objects.filter(student_id=get_obj).update(
                course_start_date=first_monday,
                course_completion_date=get_course_dates,
                target_rank=target,
                daily_pace=daily_hours,
            )

            latest_obj=payment_allow_days.objects.last()
            get_academic=academic_details.objects.filter(student_id=get_obj).first()   
            get_course = course.objects.filter(id=get_academic.course_id.id).first() 
            thisYear_totalFee=check_course(get_course.id)
            student_payments.objects.create(
                student_id      = get_obj ,
                allow_days      = latest_obj  ,
                allow_date      = pd.to_datetime(first_monday) + pd.DateOffset(weeks=4), 
                course_id       = get_course ,
                course_dates_id = get_course_dates ,
                total_amount    = get_course.course_fee ,
                remain_amount   = get_course.course_fee ,
            )
            
            daily_hours=''
            start_date=''
            end_date=''
           
            if get_course:
                    course_id=get_course.id
                    course_name=get_course.name
                    course_fee=get_course.course_fee
                    course_type=get_course.get_course_type_display()
            else:
                course_id=''
                course_name=''  
                course_fee=''
                course_type=''  

            # calculate time of all topic in a course
            toatl_time_of_course=0
            if not get_academic.stream_id:
                stream_id=''
                stream_name=''
            else:
                stream_id=get_academic.stream_id.id
                stream_name=get_academic.stream_id.stream_name  
            if not get_academic.daily_pace:
                daily_hours = ''
            else:
                daily_hours = get_academic.daily_pace

            if not get_academic.course_start_date:
                start_date = ''
            else:
                start_date = get_academic.course_start_date    
            if not get_academic.target_rank:
                targetRank=''
            else:
                targetRank=get_academic.target_rank    
            
            if not get_academic.course_completion_date:
                end_date = ''
                standard_hours=''
            else:
                end_date = get_academic.course_completion_date.course_completion_date  
                for sub in get_course.subjects.all():
                    get_chps=chapter.objects.filter(subjects_id=sub)
                    for chp in get_chps:
                        get_topics=topic.objects.filter(chapter_id=chp)
                        for tpc in get_topics:
                            toatl_time_of_course+=int(tpc.duration)  
                
                into_hours=toatl_time_of_course/60     
                get_course_dates = get_academic.course_completion_date
                get_monday=get_academic.course_start_date

                get_days=(end_date-get_monday).days
                get_weeks=get_days/7
                weeks=round(get_weeks)
                study_days=get_weeks*6
                standard_hours=into_hours/study_days
            
            if not lurnifighter_badges_status.objects.filter(student_id=get_obj).last():
                badge=''
            else:
                get_badge=lurnifighter_badges_status.objects.filter(student_id=get_obj).last()
                badge=get_badge.lurnifighter_badges_id.level_name    

            get_cash=lurnifighter_cashcoupons.objects.filter(student_id=get_obj)
            cash=0
            remain_cash = 0
            refer_cash = 0
            if get_cash:
                for g in get_cash:
                    cash += g.cash_coupons_id.coupon_value
                    if g.got_for == 'Refer':
                        if g.cash_coupons_id.expires_at > date.today():
                            if not  g.is_used:
                                refer_cash += g.cash_coupons_id.coupon_value 
                    else:
                        remain_cash += g.cash_coupons_id.coupon_value 
            crowns = 0
            chs=lurnifighter_daily_challenge.objects.filter(student_id=get_obj)
            if chs:
                for ch in chs:
                    crowns += ch.total_crown 

            payment_obj = student_payments.objects.filter(student_id=get_obj).first()

            if not get_academic.academic_limits_id:
                limit = 0
            else:
                limit=get_academic.academic_limits_id.limit_no
            data={
                'status':"success",
                'status_code':200,
                'hasError':False,
                'message':"Registration Completed",
                'data':{
                    'student_id':get_obj.id, 
                    'image':get_obj.image.url,
                    'phone': get_obj.phone,
                    'email':email,
                    'student_name':get_obj.student_name,
                    'daily_hours':daily_hours,
                    "standard_hours": str(float("{0:.2f}".format(standard_hours))),
                    'total_weeks':weeks,
                    'stream_id':stream_id,
                    'stream_name':stream_name,
                    'course_id':course_id,
                    'course_name':course_name,
                    'course_fee':course_fee,
                    'course_type':course_type,
                    'total_time':toatl_time_of_course,
                    'course_start_date':start_date,
                    'course_end_date':end_date,
                    'target_rank':targetRank,
                    'trophy':lurnifighter_levels.objects.filter(student_id=get_obj,level_status="completed").count(),
                    'badge':badge,
                    'academic_update_limit':limit,
                    'academic_update_count':get_academic.academic_update_count,
                    'cash_coupons':lurnifighter_cashcoupons.objects.filter(student_id=get_obj).count(),
                    'cash':cash,
                    'crowns':crowns,
                    'remain_cash':remain_cash,
                    'refer_cash':refer_cash,
                    'total_fee':payment_obj.total_amount,
                    'this_year_fee'         :thisYear_totalFee ,
                    'remain_fee':payment_obj.remain_amount,
                    'paid_fee':payment_obj.paid_amount,
                    'due_date':payment_obj.allow_date,
                    'is_subscribed':payment_obj.total_paid,
                    'address':address ,
                    'city':city ,
                    'state':state ,
                    'dob':dob ,
                    'pin_code':pin_code,
                    'coaching_name':coaching_name,
                    'coaching_city':coaching_city,
                    'course_program':course_program,
                    'token':token_api(phone),
                    'is_exists':True,
                }
                }
            return JsonResponse(data)
        except Exception as e:
            print(e)
            data={
                'status':"failed",
                'status_code':400,
                'hasError':True,
                'message':str(e),
                'data':{}
            }
            return JsonResponse(data)

  


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication]) 
def student_profile_api(request):
    get_student = student_profile.objects.get(user=request.user)

    if get_student.email:
        email = get_student.email
    else:
        email = ''
    if get_student.address:
            address = get_student.address
    else:
        address = ''
    if get_student.city:
        city = get_student.city
    else:
        city = ''
    if get_student.state:
        state = get_student.state
    else:
        state = ''
    if get_student.date_of_birth:
        dob = get_student.date_of_birth
    else:
        dob = ''

    if get_student.pin_code:
        pin_code = get_student.pin_code
    else:
        pin_code = ''

    if get_student.coaching_name:
        coaching_name = get_student.coaching_name
    else:
        coaching_name = ''

    if get_student.coaching_city:
        coaching_city = get_student.coaching_city
    else:
        coaching_city = ''

    if get_student.course_program:
        course_program = get_student.course_program
    else:
        course_program = ''      

    get_academic=academic_details.objects.filter(student_id=get_student).first()
    daily_hours=''
    start_date=''
    end_date=''
    standard_hours=''
    get_course = course.objects.filter(id=get_academic.course_id.id).first()
    thisYear_totalFee=check_course(get_course.id)
    
    if get_course:
        course_id=get_course.id
        course_name=get_course.name
        course_fee=get_course.course_fee
        course_type=get_course.get_course_type_display()
    else:
        course_id=''
        course_name=''  
        course_fee=''
        course_type=''  
    # calculate time of all topic in a course
    toatl_time_of_course=0
    if not get_academic.stream_id:
        stream_id=0
        stream_name=''
    else:
        stream_id=get_academic.stream_id.id
        stream_name=get_academic.stream_id.stream_name  
    if not get_academic.daily_pace:
        daily_hours = ''
    else:
        daily_hours = get_academic.daily_pace

    if not get_academic.course_start_date:
        start_date = ''
    else:
        start_date = get_academic.course_start_date    
    if not get_academic.target_rank:
        targetRank=''
    else:
        targetRank=get_academic.target_rank    
    
    if not get_academic.course_completion_date:
        end_date = ''
        standard_hours=''
    else:
        end_date = get_academic.course_completion_date.course_completion_date  
        for sub in get_course.subjects.all():
            get_chps=chapter.objects.filter(subjects_id=sub)
            for chp in get_chps:
                get_topics=topic.objects.filter(chapter_id=chp)
                for tpc in get_topics:
                    toatl_time_of_course+=int(tpc.duration)  
        
        
        into_hours=toatl_time_of_course/60     # convert into hours
        get_monday=get_academic.course_start_date  # get monday of student

        get_days=(end_date-get_monday).days
        get_weeks=get_days/7
        weeks=round(get_weeks)
        study_days=get_weeks*6
        standard_hours=into_hours/study_days
    if not lurnifighter_badges_status.objects.filter(student_id=get_student).last():
        badge=''
    else:
        get_badge=lurnifighter_badges_status.objects.filter(student_id=get_student).last()
        badge=get_badge.lurnifighter_badges_id.level_name    
    
    get_cash=lurnifighter_cashcoupons.objects.filter(student_id=get_student)
    cash=0
    remain_cash = 0
    refer_cash = 0
    if get_cash:
        for g in get_cash:
            cash += g.cash_coupons_id.coupon_value
            if g.got_for == 'Refer':
                if g.cash_coupons_id.expires_at > date.today():
                    if not  g.is_used:
                        refer_cash += g.cash_coupons_id.coupon_value 
            else:
                remain_cash += g.cash_coupons_id.coupon_value


    crowns = 0
    chs=lurnifighter_daily_challenge.objects.filter(student_id=get_student)
    if chs:
        for ch in chs:
            crowns += ch.total_crown 

    payment_obj = student_payments.objects.filter(student_id=get_student).first()           

    if not get_academic.academic_limits_id:
        limit = 0
    else:
        limit=get_academic.academic_limits_id.limit_no
    
    context ={
        'status':'success',
        'status_code':200,
        'hasError':False,
        'message':'Welcome Back',
        'data':{
            'student_id'            :get_student.id,
            'image'                 :get_student.image.url,
            'phone'                 :get_student.phone,
            'email'                 :email,
            'student_name'          :get_student.student_name,
            'daily_hours'           :daily_hours,
            'standard_hours'        :str(float("{0:.2f}".format(standard_hours))),
            'total_weeks'           :weeks,
            'stream_id'             :stream_id,
            'stream_name'           :stream_name,
            'course_id'             :course_id,
            'course_name'           :course_name,
            'course_fee'            :course_fee,
            'course_type'           :course_type,
            'total_time'            :toatl_time_of_course,
            'course_start_date'     :start_date,
            'course_end_date'       :end_date,
            'target_rank'           :targetRank,
            'trophy'                :lurnifighter_levels.objects.filter(student_id=get_student ,level_status="completed").count(),
            'badge'                 :badge,
            'academic_update_limit' :limit ,
            'academic_update_count' :get_academic.academic_update_count,
            'cash_coupons'          :lurnifighter_cashcoupons.objects.filter(student_id=get_student).count(),
            'cash'                  :cash,
            'crowns'                :crowns,
            'remain_cash'           :remain_cash,
            'refer_cash'            :refer_cash,
            'total_fee'             :payment_obj.total_amount,
            'this_year_fee'         :thisYear_totalFee ,
            'remain_fee'            :payment_obj.remain_amount,
            'paid_fee'              :payment_obj.paid_amount,
            'due_date'              :payment_obj.allow_date,
            'is_subscribed'         :payment_obj.total_paid,
            'address'               :address ,
            'city'                  :city ,
            'state'                 :state ,
            'dob'                   :dob ,
            'pin_code'              :pin_code,
            'coaching_name'         :coaching_name,
            'coaching_city'         :coaching_city,
            'course_program'        :course_program,
            'token'                 :token_api(get_student.phone),
            'is_exists'             :True,
    }        
    }
    return JsonResponse(context)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])         
def profile_pic(request):
    try:
        if request.method == 'POST':
            obj=student_profile.objects.get(user=request.user)
            serializer = Profile_PIC(obj,data=request.data)
            if not serializer.is_valid():
                data={
                        'status':'failed',
                        'status_code':400,
                        'hasError':True,
                        'message':'Profile pic upload failed',
                        'data':{}
                                     }
                return JsonResponse(data)                     

            if serializer.is_valid():
                serializer.save()
                data={
                    'status':'success',
                    'status_code':200,
                    'hasError':False,
                    'message':'Profile pic upload successfully',
                    'data':{}
                                    }
                return JsonResponse(data)
    except Exception as e:
        data={
            'status':'failed',
            'status_code':400,
            'hasError':True,
            'message':'Profile pic upload failed',
            'data':{},
            'error':str(e)
        }
        return JsonResponse(data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])  
def profile_update(request):
    try:
        if request.method == 'POST':
            obj=student_profile.objects.get(user=request.user)
            serializer = Profile_Update(obj,data=request.data)
            if not serializer.is_valid():
                data={
                        'status':'failed',
                        'status_code':400,
                        'hasError':True,
                        'message':'Profile Update failed',
                        'data':{}
                                     }
                return JsonResponse(data)                     

            if serializer.is_valid():
                serializer.save()
                data={
                    'status':'success',
                    'status_code':200,
                    'hasError':False,
                    'message':'Profile Update successfully',
                    'data':{}
                                    }
                return JsonResponse(data)
    except Exception as e:
        data={
            'status':'failed',
            'status_code':400,
            'hasError':True,
            'message':'Profile Update failed',
            'data':{}
        }
        return JsonResponse(data)   