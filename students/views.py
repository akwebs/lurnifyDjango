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
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])       
def course_structure(request):
    try:
        get_student         = student_profile.objects.filter(user=request.user).first()
        get_academic_obj    = academic_details.objects.filter(student_id=get_student).first()
        get_course          = course.objects.filter(id=get_academic_obj.course_id.id).first()
        course_subjects     = get_course.subjects.all()
        course_units        = []
        subject_duration = 0
        chapter_duration = 0
        topic_duration = 0
        unit_duration=0   
        toatl_time_of_course=0
        
        for sub in get_course.subjects.all():
            get_chps=chapter.objects.filter(subjects_id=sub)
            for chp in get_chps:
                get_topics=topic.objects.filter(chapter_id=chp)
                for tpc in get_topics:
                    toatl_time_of_course+=int(tpc.duration)
        
        
        course_structure={
            "course_id":get_course.id,
            "course_duration":str(toatl_time_of_course),
            "course_name":get_course.name,
            "courseContent":[]
        }            
        subject_list=[]
        for sub in course_subjects:
            subs={
                'id':sub.id,
                "subject":sub.subject_name,
                "subject_duration":'',
                "subject_units":[]
            }
            subject_units=[]
            for ut in sub.subjectUnit.all():
                uts={
                    'id':ut.id,
                    'unit_name':ut.unit_name,
                    'unit_chapters':[]
                    }
                unit_chapters=[]
                for ch in ut.unitChapter.all():
                    chs={
                        'id':ch.id,
                        'chapter_name':ch.chapter_name,
                        'chapter_duration':'',
                    }
                    chapter_topics=[]
                    for t in ch.chapterTopic.all():
                        tps={
                            'id':t.id,
                            'topic_name':t.topic_name,
                            "serial_number":t.serial_number,
                            "duration":t.duration,
                            "topic_importance":t.topic_importance,
                            "topic_lable":t.topic_lable
                        }
                        topic_subtopics=[]
                        topic_duration += int(t.duration)
                        for st in t.topicSubtopic.all():
                            sts={
                                'id':st.id,
                                'subtopic_name':st.subtopic_name,
                            }
                            subtopic_text=[]
                            for txt in st.subtopicText.all():
                                txts={
                                    'id':txt.id,
                                    'subtopic_text':txt.subtopic_text,
                                }
                                subtopic_text.append(txts)
                            sts['subtopic_text']=subtopic_text   
                            topic_subtopics.append(sts)
                        tps['topic_subtopics']=topic_subtopics    
                        chapter_topics.append(tps)
                    chs['chapter_topics']=chapter_topics
                    chs['chapter_duration']=topic_duration 
                    topic_duration=0   
                    unit_duration += chs['chapter_duration']
                    unit_chapters.append(chs)
                uts['unit_chapters']=unit_chapters
                uts['unit_duration']=unit_duration
                unit_duration=0    
                subject_units.append(uts)
                subject_duration += uts['unit_duration']
            subs['subject_units']=subject_units
            subs['subject_duration']=subject_duration
            subject_duration=0
            subject_list.append(subs)
        course_structure['courseContent']=subject_list            
        data={
            'status':'success',
            'status_code':200,
            'hasError':False,
            'message':'Course Structure',
            'data':{
                
                'course_structure':course_structure 

            }
            
            }
        return JsonResponse(data)
    except Exception as e:
        print(e)
        data={
            'status':'failed',
            'status_code':500,
            'hasError':True,
            'message':'Something went wrong',
            'data':{}
        }  
        return JsonResponse(data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication]) 
def complete_register(request):
    courses_dates=[]
    get_student         = student_profile.objects.filter(user=request.user).first()
    get_academic_obj    = academic_details.objects.filter(student_id=get_student).first()
    get_course          = course.objects.filter(id=get_academic_obj.course_id.id).first()
    # calculate time of all topic in a course
    toatl_time_of_course=0
    for sub in get_course.subjects.all():
        get_chps=chapter.objects.filter(subjects_id=sub)
        for chp in get_chps:
            get_topics=topic.objects.filter(chapter_id=chp)
            for tpc in get_topics:
                toatl_time_of_course+=int(tpc.duration)
    
    
    into_hours=toatl_time_of_course/60          
    get_course_dates    = course_dates.objects.filter(course_id=get_course)
    onDay = lambda date, day: date + datetime.timedelta(days=(day-date.weekday()+7)%7)
    get_monday=onDay(datetime.date.today(),0)

    for c in get_course_dates:
        total_days=c.course_completion_date-get_monday
        get_days=abs(c.course_completion_date-get_monday).days
        get_weeks=get_days//7
        study_days=get_weeks*6
        get_hours=into_hours/study_days
        
        list_of_d={
            'course_id':c.id,
            'course_date':c.course_completion_date.strftime("%d %B %Y | %A"),
            'get_hours':str(float("{0:.2f}".format(get_hours))),
            'image':c.image.url,
            'full_date':c.course_completion_date,
        }   
        courses_dates.append(list_of_d)
    
    daily_hours=''
    start_date=''
    end_date=''
    
    
    if not get_academic_obj.daily_pace:
        daily_hours = ''
    else:
        daily_hours = get_academic_obj.daily_pace

    if not get_academic_obj.course_start_date:
        start_date = ''
    else:
        start_date = get_academic_obj.course_start_date    

    if not get_academic_obj.course_completion_date:
        end_date = ''
    else:
        end_date = get_academic_obj.course_completion_date.course_completion_date 
    main_data={
        "status":"success",
        "status_code":200,
        "message":"complete registration",
        'hasError':False,
        "data":{
            'student_id':get_student.id,
            'student_name':get_student.student_name,
            'daily_hours':daily_hours,
            'course_start_date':start_date,
            'course_end_date':end_date,
            "student_name":get_student.student_name,
            "courses_dates":courses_dates,
            "firstMonday":str(get_monday),
            
        }   
    }
    return JsonResponse(main_data)
        
        
        
        

  

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication]) 
def update_study_pattern(request):
    try:
        get_obj = student_profile.objects.get(user=request.user)
        phone = get_obj.phone
        limit = academic_limits.objects.last()
        msg=''
        print(limit)
        get_data=json.loads(request.body)
        course_date_id      =   get_data['course_dates_id']
        target              =   get_data['target_rank']
        daily_hours         =   get_data['daily_hours']


        get_academic_obj=academic_details.objects.filter(student_id=get_obj).first()
        if not get_academic_obj.academic_limits_id:
            get_academic_obj.academic_limits_id=limit
            get_academic_obj.save()    

        if get_academic_obj.academic_limits_id.limit_no <= get_academic_obj.academic_update_count:
            msg='you have reached your limit of academic journey updates'

        else:    
            if course_date_id: 
                get_course_dates = course_dates.objects.filter(id=course_date_id).first()
                get_academic_obj.course_completion_date=get_course_dates
                get_academic_obj.save()
            if target:
                get_academic_obj.target_rank=target
                get_academic_obj.save()
            if daily_hours:
                get_academic_obj.daily_pace=daily_hours
                get_academic_obj.save()       

            get_academic_obj.academic_update_count += 1
            get_academic_obj.save()
            
            if get_academic_obj.academic_limits_id.limit_no - get_academic_obj.academic_update_count == 0:
                 msg="You have updated your academic journey right now . you have reached your limit of academic journey updates"
            else:    
                msg=f"You have updates your academic journey right now. Now you can update only {get_academic_obj.academic_limits_id.limit_no - get_academic_obj.academic_update_count} time"
            
                             
        get_academic=academic_details.objects.filter(student_id=get_obj).first()

        # same response as check-user API    
        get_course = course.objects.filter(id=get_academic.course_id.id).first() 

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
        if get_cash:
            for g in get_cash:
                cash += g.cash_coupons_id.coupon_value

        crowns = 0
        chs=lurnifighter_daily_challenge.objects.filter(student_id=get_obj)
        if chs:
            for ch in chs:
                crowns += ch.total_crown
        # End  response 
        context={
            'status':'success',
            'status_code':200,
            'hasError':False,
            'message':msg,
            'data':{
                'student_id':get_obj.id,
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
                'academic_update_limit':get_academic.academic_limits_id.limit_no,
                'academic_update_count':get_academic.academic_update_count,
                'cash_coupons':lurnifighter_cashcoupons.objects.filter(student_id=get_obj).count(),
                'cash':cash,
                'crowns':crowns,
                'token':token_api(phone),
                'is_exists':True,
            }
            }
        return JsonResponse(context) 
    except Exception as e:
        context={
            'status':'error',
            'status_code':500,
            'hasError':True,
            'message':'Study Pattern not updated',
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
            },
            'error':str(e)
            }
        return JsonResponse(context)    



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])       
def lurnify_home(request):
    try:
        courses_dates=[]
        get_student =    student_profile.objects.filter(user=request.user).first()
        get_academic_obj = academic_details.objects.filter(student_id=get_student).first()
        get_course = course.objects.filter(id=get_academic_obj.course_id.id).first()
        get_course_dates = course_dates.objects.filter(course_id=get_course)
        for c in get_course_dates:
            list_of_d={
                'course_id':c.course_id.id,
                'course_date':c.course_completion_date,
            }   
            courses_dates.append(list_of_d)
        get_monday=""   
        if get_student.firstMonday:
            get_monday=get_student.firstMonday
        
        main_data={
            "status":"success",
            "status_code":200,
            "message":"welcome home",
             'hasError':False,
            "data":{
                'student_id':get_student.id,
                "student_name":get_student.student_name,
                "first_monday":get_monday,
            }
            
        }
        return JsonResponse(main_data)
    except Exception as e:
        data={
            "status":"failed",
            "status_code":500,
             'hasError':True,
            "message":"something went wrong please contact to administer or call 8938019494",
            "error":str(e),
            "data":{}

        }    
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])          
def all_lurnifighter_badges(request):
    try:
        get_student = student_profile.objects.filter(user=request.user).first()
        get_badges=lurnifighter_badges.objects.all()
        badges_list=[]
        referrals_list=[]
        
        lock_current = False
        for b in get_badges:
            get_objs=lurnifighter_badges_status.objects.filter(student_id=get_student,lurnifighter_badges_id=b,is_completed=True)
            if get_objs:
                get_count= weekly_challange.objects.filter(lurnifighter_badges_id=b).count()
                list_of_d={
                    'badge_id':b.id,
                    'badge_name':b.level_name,
                    'weekly_challenges':get_count,
                    'weekly_challenges_completed':get_count,
                    "status": True,
                    "payment":False,
                    "lock":False,
                 
                }
                badges_list.append(list_of_d)
            else:
                get_count= weekly_challange.objects.filter(lurnifighter_badges_id=b)     
                completed_count=0
                lock_current = False
                for g in get_count:
                    check_comp=lurnifighter_levels.objects.filter(weekly_challange_id=g , student_id=get_student , level_status='completed')  
                    check_incomp=lurnifighter_levels.objects.filter(weekly_challange_id=g , student_id=get_student , level_status='incomplete')
                    if check_comp:
                        completed_count=check_comp.count() 
                        lock_current = True 
                    if check_incomp:
                        lock_current = True                     
                list_of_d={
                    'badge_id':b.id,
                    'badge_name':b.level_name,
                    'weekly_challenges':get_count.count(),
                     'weekly_challenges_completed':completed_count,
                    "status": False,
                    "payment":False,
                    "lock":lock_current,
                }
                badges_list.append(list_of_d)
        get_referrals=lurnifighter_referral.objects.all()  
        for r in get_referrals:
            dt={
                "referral_id": r.id,
                "referral_name": r.badge_name,
                "freinds": r.reffrral_count,
                "description":r.description,
                "top": r.top,
                "status": False,
                
            }  
            referrals_list.append(dt) 


            
        context={
            "status":"success",
            "status_code":200,
            "message":"Badges Found",
            'hasError':False,
            'data':{
            'student_id':get_student.id,
            'badges':badges_list,
            'referrals':referrals_list,
            
            }

        }  
        return JsonResponse(context)          
    except Exception as e:
        context={
            "status":"failed",
            "status_code":500,
             'hasError':True,
            "message":"something went wrong please contact to administer",
            "error":str(e),
            "data":{
            'student_id':0,
            'badges':[],
            }

        } 
        return JsonResponse(context)       



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])   
def challenge_accept_view(request):
    get_student = student_profile.objects.filter(user=request.user).first()
    get_weeks=weekly_challange.objects.all()
    challenge={}
    reward={}
    for g in get_weeks:
        if lurnifighter_levels.objects.filter(weekly_challange_id=g , student_id=get_student , level_status='completed').exists():
            pass
        elif lurnifighter_levels.objects.filter(weekly_challange_id=g , student_id=get_student , level_status='incomplete').exists():
            rewd=weekly_reward.objects.filter(weekly_challange_id=g).first()
            if rewd:
                reward={
                'trophy':rewd.trophy,
                'no_of_coins':rewd.no_of_coins,
                'refer_freind_coupons':rewd.refer_freind_coupons,
                'cash_coupons':rewd.cash_coupons_id.count(),
                }
            prg=lurnifighter_levels.objects.filter(weekly_challange_id=g , student_id=get_student , level_status='incomplete').first()    
            ids=prg.id
            status=True
            weekName=prg.weekly_challange_id.week_name
            challenge={
            'total_study_hours':g.total_study_hours,
            'pr_total_study_hours':prg.total_study_hours,
            'total_test':g.total_test,
            'pr_total_test':prg.total_test,
            'total_crowns':g.total_crowns,
            'pr_total_crowns':prg.total_crowns,
            'refer_freinds':g.refer_freinds,
            'pr_refer_freinds':prg.refer_freinds,
            'test_performance':g.test_performances,
            'pr_test_performance':prg.test_performances,
            'study_effectiveness':g.study_effectiveness,
            'pr_study_effectiveness':prg.study_effectiveness,
            'status':status,
            }
            break
        else:
            rewd=weekly_reward.objects.filter(weekly_challange_id=g).first()
            if rewd:
                reward={
                'trophy':rewd.trophy,
                'no_of_coins':rewd.no_of_coins,
                'refer_freind_coupons':rewd.refer_freind_coupons,
                'cash_coupons':rewd.cash_coupons_id.count(),
                }

            ids=g.id
            weekName=g.week_name
            status=False
            challenge={
                'total_study_hours':g.total_study_hours,
                'pr_total_study_hours':0.0,
                'total_test':g.total_test,
                'pr_total_test':0,
                'total_crowns':g.total_crowns,
                'pr_total_crowns':0,    
                'refer_freinds':g.refer_freinds,
                'pr_refer_freinds':0,
                'test_performance':g.test_performances,
                'pr_test_performance':0.0,
                'study_effectiveness':g.study_effectiveness,
                'pr_study_effectiveness':0,
                 'status':status,
                }
            break
    context={
        'status':'success',
        'status_code':200,
        'hasError':False,
        'data':{
            'id':ids,
            'week_name':weekName,
            'challenge':challenge,
            'reward':reward,
            'status':status
        }
    }    
    return JsonResponse(context)  


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])   
def challenge_accepted(request , pk):
    get_student = student_profile.objects.filter(user=request.user).first()
    get_week=weekly_challange.objects.get(id=pk)

    if lurnifighter_levels.objects.filter(weekly_challange_id=get_week , student_id=get_student).exists():
        context={
        'status':'failed',
        'status_code':400,
        'hasError':True,
        'message':'this challenge already accepted',
        'data':{}
    }
        return JsonResponse(context)

    #   if user is accepte challenge for first time
    if get_week.week_number == 1 :
        get_badge=lurnifighter_badges.objects.filter(level_name='Welcome').first()
        lurnifighter_badges_status.objects.create(
            student_id=get_student,
            lurnifighter_badges_id=get_badge,
            is_completed=True )

            #end accept  challenge
    lurnifighter_levels.objects.create(
        student_id = get_student,
        weekly_challange_id =  get_week ,
        weekly_reward_id = weekly_reward.objects.filter(weekly_challange_id=get_week).first(),
        level_status='incomplete'
    )        
    context={
        'status':'success',
        'status_code':200,
        'hasError':False,
        'message':'challenge accepted successfully',
        'data':{}
    }
    return JsonResponse(context)






@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])   
def sync_challenge(request , pk):
    get_student = student_profile.objects.filter(user=request.user).first()
    get_level = lurnifighter_levels.objects.get(id=pk)
    progress_week = get_level.weekly_challange_id
    get_data=json.loads(request.body)
    study = get_data['study_hours']
    given_test = get_data['total_test']
    crowns = get_data['crowns']
    test_performance = get_data['test_performance']
    study_effectiveness = get_data['study_effectiveness']

    is_study = False
    is_given_test = False
    is_crowns = False 
    is_test_performance = False
    is_study_effectiveness = False  
    is_completed = False
    is_referral_freind = False

    if study:
        if get_level.total_study_hours >= progress_week.total_study_hours :
            is_study = True
        else:
            get_level.total_study_hours   += float(study)
            get_level.save()
    if given_test:
        if get_level.total_test >= progress_week.total_test :
            is_given_test = True
        else:
            get_level.total_test += int(given_test)
            get_level.save()
    if crowns:
        if get_level.total_crowns >= progress_week.total_crowns :
            is_crowns = True
        else:
            get_level.total_crowns += int(crowns)
            get_level.save()
    if test_performance:
        if get_level.test_performances >= progress_week.test_performances :
            is_test_performance = True
        else:
            get_level.test_performances += float(test_performance)
            get_level.save()
    if study_effectiveness:
        if get_level.study_effectiveness  >= progress_week.study_effectiveness :
            is_study_effectiveness = True
        else:
            get_level.study_effectiveness += int(study_effectiveness)
            get_level.save()
    if is_study and is_given_test and is_crowns and is_test_performance and is_study_effectiveness:
        is_completed = True 
        get_reward=weekly_reward.objects.filter(weekly_challange_id=progress_week).first()
        for reward in get_reward.cash_coupons_id.all():
            lurnifighter_cashcoupons.objects.create(
                student_id=get_student,
                cash_coupons_id=reward,
                got_for=f"got reward from weekly challnege, reward id {get_reward.id}",
            )
        lurnifighter_coupons.objects.create(
        student_id=get_student,
        weekly_challange_id=progress_week,
        weekly_reward_id=get_reward,
        )    
        get_level.level_status = 'completed'
        get_level.save() 
        get_badge=lurnifighter_badges.objects.filter(id=get_level.weekly_challange_id.lurnifighter_badges_id.id).first()
        get_all_weeks=weekly_challange.objects.filter(lurnifighter_badges_id=get_badge)
        for a_w in get_all_weeks:
            incom_weeks =lurnifighter_levels.objects.filter(weekly_challange_id=a_w ,level_status='incompleted',student_id=get_student).count()
            if incom_weeks == 0:
                lurnifighter_badges_status.objects.create(lurnifighter_badges_id=get_badge,
                student_id=get_student, 
                is_completed=True
                )
    context={
        'status':'success',
        'status_code':200,
        'hasError':False,
        'message':'challenge synced successfully',
        'data':{
            'is_study':is_study,
            'is_given_test':is_given_test,
            'is_crowns':is_crowns,
            'is_test_performance':is_test_performance,
            'is_study_effectiveness':is_study_effectiveness,
            'is_referral_freind':is_referral_freind,
            'is_completed':is_completed
        }
    }    
    return JsonResponse(context)        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])  
def trophy_home(request):
    get_student = student_profile.objects.filter(user=request.user).first()
    get_weeks=lurnifighter_levels.objects.filter(student_id=get_student , level_status='completed')
    
    weeks_list=[]
    for weeks in get_weeks:
        dt={
            'id':weeks.id,
            'week_number': weeks.weekly_challange_id.week_name ,
        }
        weeks_list.append(dt)

    context={
        'status':'success',
        'status_code':200,
        'hasError':False,
        'message':"list found successfully",
        'data':{
            'weeks':weeks_list
        }
    }
    return JsonResponse(context)    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])  
def trophy_view(request , pk):
    get_student = student_profile.objects.filter(user=request.user).first()
    get_challenge=lurnifighter_levels.objects.filter(student_id=get_student , id=pk).first()

    challenge={
            'total_study_hours':get_challenge.weekly_challange_id.total_study_hours,
            'total_test':get_challenge.weekly_challange_id.total_test,
            'total_crowns':get_challenge.weekly_challange_id.total_crowns,
            'refer_freinds':get_challenge.weekly_challange_id.refer_freinds,
            'test_performance':get_challenge.weekly_challange_id.test_performances,
            'study_effectiveness':get_challenge.weekly_challange_id.study_effectiveness,
            }
    
    reward={
                'trophy':get_challenge.weekly_reward_id.trophy,
                'no_of_coins':get_challenge.weekly_reward_id.no_of_coins,
                'refer_freind_coupons':get_challenge.weekly_reward_id.refer_freind_coupons,
                'cash_coupons':get_challenge.weekly_reward_id.cash_coupons_id.count(),
        } 
    context={
        'status':'success',
        'status_code':200,
        'hasError':False,
        'message':"list found successfully",
        'data':{
            'challenge':challenge,
            'reward':reward,
        }
    }
    return JsonResponse(context)       



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication]) 
def monthly_certificate_list(request):
    get_student = student_profile.objects.filter(user=request.user).first()
    datem = date.today().strftime("%b")
    this_year=date.today().strftime("%Y")
    #print(strptime(datem,'%b').tm_mon) month number
    monthh_filter=  lurnifighter_levels.objects.filter(level_status='completed',
                            student_id=get_student,
                            created_at__month=strptime(datem,'%b').tm_mon) 

    mk_list=[]
    # if monthh_filter.count() >= 2:
    #     test_perfor=0.0
    #     for mn in monthh_filter:
    #         test_perfor += mn.test_performances
    #     print()
    #     if test_perfor > int(75):
    #         print("yes")    

    # else:
    #     print("need to complete atleast two weekly challange in a month")

    get_all=monthly_certificate.objects.filter(student_id=get_student)

    for a in get_all:
        dt={
            "student_id":a.student_id.id,
            "test_performance":a.test_performance,
            "criteria_performance":a.monthly_challange_criteria_id.test_performance,
            "weekly_challenge":a.weekly_challange,
            "weekly_criteria":a.monthly_challange_criteria_id.weekly_challange,
            "month_name":f"{a.month_name}-{this_year}",
            "certificate":a.certificate,
        }
        mk_list.append(dt)
                         
    context={
        'status':'success',
        'status_code':200,
        'hasError':False,
        'message':"list found successfully",
        'data':{
            'certificates':mk_list
        }
    }
    return JsonResponse(context)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication]) 
def spin_wheel_item(request):
    get_challenge=daily_challenge.objects.filter(to_day=date.today()).first()
    mk_list=[]
    if get_challenge:
        ids = get_challenge.id
        crn = get_challenge.crown
        for g in get_challenge.test_and_study_id.all():
            dt={
                'id':g.id,
                'title':g.title,
                'sub_title':g.sub_title,
                'coins':g.coins,
                'crowns':g.crowns,
            }
            mk_list.append(dt)
    else:
        ids=0
        crn=0
    context={
        'status':'success',
        'status_code':200,
        'hasError':False,
        'message':"list found successfully",
        'data':{
            'id':ids,
            'spin_wheel_item':mk_list,
            'crowns':crn,
        }
    }    
    return JsonResponse(context)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication]) 
def daily_challenge_accept(request , pk):
    get_student = student_profile.objects.filter(user=request.user).first()
    get_daily  = test_and_study.objects.get(id=pk)

    get_obj=lurnifighter_daily_challenge.objects.create(
        student_id = get_student ,
        test_and_study_id = get_daily,
        total_coins = get_daily.coins ,
        total_crown = get_daily.crowns ,
    )

    context = {
        'status':'success',
        'status_code':200,
        'hasError':False,
        'message':"challenge accepted successfully",
        'data':{
            "coins": get_obj.total_coins ,
            'crowns': get_obj.total_crown ,
        }
    }
    return JsonResponse(context)





@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication]) 
def student_cash_coupons(request):
    get_student = student_profile.objects.filter(user=request.user).first()
    get_all=lurnifighter_cashcoupons.objects.filter(student_id=get_student)
    mk_list=[]
    for a in get_all:
        dt={
            'id':a.id,
            "got_for":a.got_for,
            "cash_value":a.cash_coupons_id.coupon_value,
            "is_used":a.is_used,
            "is_opened":a.is_opened,
            "created_at":a.created_at,
        }
        mk_list.append(dt)
    
    context={
        'status':'success',
        'status_code':200,
        'hasError':False,
        'message':"coupons found successfully",
        'data':{
            'coupons':mk_list
        }
    }
    return JsonResponse(context)  
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication]) 
def cash_coupon_status(request):
    try:
        get_student = student_profile.objects.filter(user=request.user).first()
        get_data =json.loads(request.body)
        ids = get_data['id']
        is_opend = get_data['is_opened']

        if is_opend == True:
            lurnifighter_cashcoupons.objects.filter(student_id=get_student,id=ids).update(is_opened=True)

            
        context={
            'status':'success',
            'status_code':200,
            'hasError':False,
            'message':"coupons found successfully",
            'data':{}
        }
        return JsonResponse(context)
    except Exception as e:
        context={
            'status':'error',
            'status_code':400,
            'hasError':True,
            'message':"coupons not found",
            'data':{},
            'error':str(e)
        }
        return JsonResponse(context)  

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication]) 
def sync_student_study(request):
    obj=student_profile.objects.get(user=request.user)   
    serializer = StudentStudy(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()   
    else:
        context={
            'status':'error',
            'status_code':400,
            'hasError':True,
            'message':"data sync failed",
            'data':{},
            'error':serializer.errors
        }
        return JsonResponse(context)
    context={
        'status':'success',
        'status_code':200,
        'hasError':False,
        'message':"data synced successfully",
        'data':{
            
        }
    }
    return JsonResponse(context)



          

