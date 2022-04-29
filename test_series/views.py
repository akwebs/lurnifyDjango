from django.shortcuts import render ,redirect
from .models import *
from courses.models import *
from accounts.models import *
from test_series.models import *
from django.http import  JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
import requests
import json
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from django.views.decorators.csrf import csrf_exempt
import datetime
from .serializers import *



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication]) 
def test_request(request):
    get_data=json.loads(request.body)
    chapter_id=get_data['chapter_id']
    get_tests=create_test.objects.filter(chapter_id_id=chapter_id)
    test_list=[]
    for ts in get_tests:
        dt={
            'test_id':ts.id,
            'test_name':ts.test_name,
            'test_type':ts.test_type,
            'course_id':ts.course_id.id,
            'course_name':ts.course_id.name,
            'subject_id':ts.subject_id.id,
            'subject_name':ts.subject_id.subject_name,
            'chapter_id':ts.chapter_id.id,
            'chapter_name':ts.chapter_id.chapter_name,
            'topic_id':ts.topic_id.id,
            'topic_name':ts.topic_id.topic_name,
            'test_duration':ts.test_duration,
            'question_positive_marks':ts.question_positive_marks,
            'question_negative_marks':ts.question_negative_marks,
            'test_set':ts.test_set,
            'test_level':ts.test_level,
            'instructions':[],
            'questions':[]
        }
        get_questions=ts.testQuestionBank.all()
        get_list = QuestionSerializer(get_questions,many=True).data
        dt['questions']=get_list
        get_instructions=ts.createTestInstructions.all()
        get_list = InstructionSerializer(get_instructions,many=True).data
        dt['instructions']=get_list
        test_list.append(dt)

    data={
                'status':"success",
                'status_code':200,
                'hasError':False,
                'message':"Test Fetched Successfully",
                'data':{
                    'test_list':test_list
                   
                }
                        }
    return JsonResponse(data) 

        




