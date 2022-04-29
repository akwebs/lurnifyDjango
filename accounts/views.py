from all_imports.all_imports import *

# Create your views here.




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


@api_view(['POST'])
def user_login(request):
    get_data=json.loads(request.body)
    phone=get_data['phone']
    if Account.objects.filter(phone=phone).exists():
        get_student = student_profile.objects.filter(phone=phone).first()
        if get_student:
            context={
            'status': 'scucess',
            'status_code': 200,
            'hasError': False,
            'message':'Welcome Back ',
            'data':{
                'token':token_api(phone),
                'is_exists':True,
                            }
                            } 
            return JsonResponse(context)
        else:
            context={
            'status': 'failed',
            'status_code': 400,
            'hasError':True,
            'message':'You are not a student',
            'data':{
                'token':'',
                'is_exists':True,
            }
        } 
        return JsonResponse(context)
    else:
        context={
            'status': 'scucess',
            'status_code': 200,
            'hasError':False,
            'message':'Account does not exist',
            'data':{
                'token':'',
                'is_exists':False,
            }
        } 
        return JsonResponse(context)   




@api_view(['POST'])
def check_user(request):
    try:
        get_data=json.loads(request.body)
        phone=get_data['phone']
        if Account.objects.filter(phone=phone).exists():
            account = Account.objects.get(phone=phone)
            get_student = student_profile.objects.filter(user=account).first()
            if get_student:
                get_academic=academic_details.objects.filter(student_id=get_student).first()
                daily_hours=''
                start_date=''
                end_date=''
                standard_hours=''
                get_course = course.objects.filter(id=get_academic.course_id.id).first()
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
                if get_cash:
                    for g in get_cash:
                        cash += g.cash_coupons_id.coupon_value

                crowns = 0
                chs=lurnifighter_daily_challenge.objects.filter(student_id=get_student)
                if chs:
                    for ch in chs:
                        crowns += ch.total_crown

                main_data={
                    'status':'success',
                    'status_code':200,
                    'message':'welcome back',
                    'hasError':False,
                    'data':{
                        'student_id':get_student.id,
                        'student_name':get_student.student_name,
                        'daily_hours':daily_hours,
                        'standard_hours':str(float("{0:.2f}".format(standard_hours))),
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
                        'trophy':lurnifighter_levels.objects.filter(student_id=get_student , level_status="completed").count(),
                        'badge':badge,
                        'academic_update_limit':get_academic.academic_limits_id.limit_no,
                        'academic_update_count':get_academic.academic_update_count,
                        'cash_coupons':lurnifighter_cashcoupons.objects.filter(student_id=get_student).count(),
                        'cash':cash,
                        'crowns':crowns,
                        'token':token_api(phone),
                        'is_exists':True,
                    }
                    }
                return JsonResponse(main_data)
            else:
                main_data={
                'status':'failed',
                'status_code':400,
                'hasError':True,
                'message':'You are not a student',
                'data':{
                    'student_id':0,
                    'student_name':'',
                    'daily_hours':'',
                    'standard_hours':'',
                    'total_weeks':0,
                    'stream_id':0,
                    'stream_name':'',
                    'course_id':0,
                    'course_name':'',
                    'course_fee':'',
                    'course_type':'',
                    'total_time':0,
                    'course_start_date':'',
                    'course_end_date':'',
                    'target_rank':'',
                    'trophy':0,
                    'badge':'',
                    'academic_update_limit':0,
                    'academic_update_count':0,
                    'cash_coupons':0,
                    'cash':0,
                    'crowns':0,
                    'token':'',
                    'is_exists':True,
                }
            }
            return JsonResponse(main_data) 
        else:
            main_data={
                'status':'success',
                'status_code':200,
                'hasError':False,
                'message':'welcome',
                'data':{
                    'student_id':0,
                    'student_name':'',
                    'daily_hours':'',
                    'standard_hours':'',
                    'total_weeks':0,
                    'stream_id':0,
                    'stream_name':'',
                    'course_id':0,
                    'course_name':'',
                    'course_fee':'',
                    'course_type':'',
                    'total_time':0,
                    'course_start_date':'',
                    'course_end_date':'',
                    'target_rank':'',
                    'trophy':0,
                    'badge':'',
                    'academic_update_limit':0,
                    'academic_update_count':0,
                    'cash_coupons':0,
                    'cash':0,
                    'crowns':0,
                    'token':'',
                    'is_exists':False,
                }
            }
            return JsonResponse(main_data)  
    except Exception as e:
        main_data={
            'status':'error',
            'status_code':500,
            'hasError':True,
            'message':'something went wrong contact to admin',
            'data':{
                     'student_id':0,
                    'student_name':'',
                    'daily_hours':'',
                    'standard_hours':'',
                    'total_weeks':0,
                    'stream_id':0,
                    'stream_name':'',
                    'course_id':0,
                    'course_name':'',
                    'course_fee':'',
                    'course_type':'',
                    'total_time':0,
                    'course_start_date':'',
                    'course_end_date':'',
                    'target_rank':'',
                    'trophy':0,
                    'badge':'',
                    'academic_update_limit':0,
                    'academic_update_count':0,
                    'cash_coupons':0,
                    'cash':0,
                    'crowns':0,
                    'token':'',
                    'is_exists':False,
            },
            'error':str(e)
        }
        return JsonResponse(main_data)        


                

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication]) 
# def check_user(request):
#     try:
#         get_student = student_profile.objects.filter(user=request.user).first()
        
#         if get_student.email:
#             email=get_student.email
#         else:
#             email=''    
            
        
#         get_academic=academic_details.objects.filter(student_id=get_student).first()
#         daily_hours=''
#         start_date=''
#         end_date=''
#         standard_hours=''
#         get_course = course.objects.filter(id=get_academic.course_id.id).first()
#         if get_course:
#             course_id=get_course.id
#             course_name=get_course.name
#             course_fee=get_course.course_fee
#             course_type=get_course.get_course_type_display()
#         else:
#             course_id=''
#             course_name=''  
#             course_fee=''
#             course_type=''  
#         # calculate time of all topic in a course
#         toatl_time_of_course=0
#         if not get_academic.stream_id:
#             stream_id=0
#             stream_name=''
#         else:
#             stream_id=get_academic.stream_id.id
#             stream_name=get_academic.stream_id.stream_name  
#         if not get_academic.daily_pace:
#             daily_hours = ''
#         else:
#             daily_hours = get_academic.daily_pace

#         if not get_academic.course_start_date:
#             start_date = ''
#         else:
#             start_date = get_academic.course_start_date    
#         if not get_academic.target_rank:
#             targetRank=''
#         else:
#             targetRank=get_academic.target_rank    
        
#         if not get_academic.course_completion_date:
#             end_date = ''
#             standard_hours=''
#         else:
#             end_date = get_academic.course_completion_date.course_completion_date  
#             for sub in get_course.subjects.all():
#                 get_chps=chapter.objects.filter(subjects_id=sub)
#                 for chp in get_chps:
#                     get_topics=topic.objects.filter(chapter_id=chp)
#                     for tpc in get_topics:
#                         toatl_time_of_course+=int(tpc.duration)  
            
            
#             into_hours=toatl_time_of_course/60     # convert into hours
#             get_monday=get_academic.course_start_date  # get monday of student

#             get_days=(end_date-get_monday).days
#             get_weeks=get_days/7
#             weeks=round(get_weeks)
#             study_days=get_weeks*6
#             standard_hours=into_hours/study_days
#         if not lurnifighter_badges_status.objects.filter(student_id=get_student).last():
#             badge=''
#         else:
#             get_badge=lurnifighter_badges_status.objects.filter(student_id=get_student).last()
#             badge=get_badge.lurnifighter_badges_id.level_name    
        
#         get_cash=lurnifighter_cashcoupons.objects.filter(student_id=get_student)
#         cash=0
#         if get_cash:
#             for g in get_cash:
#                 cash += g.cash_coupons_id.coupon_value

#         crowns = 0
#         chs=lurnifighter_daily_challenge.objects.filter(student_id=get_student)
#         if chs:
#             for ch in chs:
#                 crowns += ch.total_crown

#         main_data={
#             'status':'success',
#             'status_code':200,
#             'message':'welcome back',
#             'hasError':False,
#             'data':{
#                 'student_id':get_student.id,
#                 'student_name':get_student.student_name,
#                 'email':email,
#                 'image':get_student.image.url,
#                 'phone':get_student.phone,
#                 'daily_hours':daily_hours,
#                 'standard_hours':str(float("{0:.2f}".format(standard_hours))),
#                 'total_weeks':weeks,
#                 'stream_id':stream_id,
#                 'stream_name':stream_name,
#                 'course_id':course_id,
#                 'course_name':course_name,
#                 'course_fee':course_fee,
#                 'course_type':course_type,
#                 'total_time':toatl_time_of_course,
#                 'course_start_date':start_date,
#                 'course_end_date':end_date,
#                 'target_rank':targetRank,
#                 'trophy':lurnifighter_levels.objects.filter(student_id=get_student , level_status="completed").count(),
#                 'badge':badge,
#                 'academic_update_limit':get_academic.academic_limits_id.limit_no,
#                 'academic_update_count':get_academic.academic_update_count,
#                 'cash_coupons':lurnifighter_cashcoupons.objects.filter(student_id=get_student).count(),
#                 'cash':cash,
#                 'crowns':crowns,
#             }
#             }
#         return JsonResponse(main_data)
           
       
#     except Exception as e:
#         main_data={
#             'status':'error',
#             'status_code':500,
#             'hasError':True,
#             'message':'something went wrong contact to admin',
#             'data':{
#             'student_id':0,
#             'student_name':'',
#             'email':'',
#             'image':'',
#             'phone':'',
#             'daily_hours':'',
#             'standard_hours':'',
#             'total_weeks':0,
#             'stream_id':0,
#             'stream_name':'',
#             'course_id':0,
#             'course_name':'',
#             'course_fee':'',
#             'course_type':'',
#             'total_time':0,
#             'course_start_date':'',
#             'course_end_date':'',
#             'target_rank':'',
#             'trophy':0,
#             'badge':'',
#             'academic_update_limit':0,
#             'academic_update_count':0,
#             'cash_coupons':0,
#             'cash':0,
#             'crowns':0,
#             },
#             'error':str(e)
#         }
#         return JsonResponse(main_data)        


@api_view(['POST'])
def user_entry(request):
    try:
        get_data=json.loads(request.body)
        phone=get_data['phone']
        name=get_data['name']
        stream_id=get_data['stream']
        course_id=get_data['course_id']
        r_code=get_data['referal_code']
        if Account.objects.filter(phone=phone).exists():
            main_data={
            'status':'success',
            'status_code':200,
            'message':'user is alredy exist',
            'hasError':False,
            'data':{
                'token':'',
                'name':'',  
                }
                }
            return JsonResponse(main_data) 
        get_obj=Account.objects.create(phone=phone , username=name)
        get_obj.set_password(phone)
        get_obj.save()
        if r_code :
           pass
        get_student = student_profile.objects.create(
                        user=get_obj , 
                        phone=phone , 
                        student_name=name ,
                        )
        get_stream=stream.objects.filter(id=stream_id).first()
        get_course=course.objects.filter(id=course_id).first()
        limit = academic_limits.objects.last()
        get_academic = academic_details.objects.create(
            student_id=get_student,
            stream_id=get_stream,
            course_id=get_course,
            academic_limits_id=limit,
        )
        main_data={
            'status':'success',
            'status_code':200,
            'message':'welcome to home',
            'hasError':False,
            'data':{
                
                'token':token_api(phone),
                'name':get_student.student_name,
                
                }
                

        }
        return JsonResponse(main_data)


    except Exception as e:
        main_data={
            'status':'fail',
            'status_code':500,
            'hasError':True,
            'message':'something went wrong , contact to adminstrator ',
            'data':{},
            'error':str(e)
        }
        return JsonResponse(main_data) 


@api_view(['POST'])
def get_streams(request):
    try:
        streams_list=[]
        all_streams=stream.objects.all()
        for st in all_streams:
            dt={
                'id':st.id,
                'name':st.stream_name,
            }
            streams_list.append(dt)

        main_data={
            'status':'success',
            'status_code':200,
            'hasError':False,
            'message':'streams found successfully',
            'data':{
                'streams':streams_list,
            },
           
        }
        return JsonResponse(main_data)

        
    except Exception as e:
        main_data={
            'status':'fail',
            'status_code':500,
            'hasError':True,
            'message':'something went wrong , contact to adminstrator',
            'data':{},
            'error':str(e)
        }
        return JsonResponse(main_data)



@api_view(['POST'])
def get_courses(request):
    try:
        get_data=json.loads(request.body)
        streamID=get_data['stream']
        course_list=[]

        get_stream=stream.objects.filter(id=streamID).first()
        print(get_stream)
        get_courses=course.objects.filter(stream_id=get_stream)
        for c in get_courses:
            get_list={
                'id':c.id,
                'course_name':c.name,
                'fee':c.course_fee,
                'year':c.get_course_type_display(),
            }
            course_list.append(get_list)
      
        main_data={
                'status':'success',
                'status_code':200,
                'hasError':False,
                'message':'welcome',
                'data':{
                    'courses':course_list,
                }
            }
        
        return JsonResponse(main_data)
       
    except Exception as e:
        main_data={
            'status':'failed',
            'status_code':500,
            'hasError':True,
            'message':str(e),
            'data':{
                'courses':[],
                'error':str(e)
            },
            
        }
        return JsonResponse(main_data)


