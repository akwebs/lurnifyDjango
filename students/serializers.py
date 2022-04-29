from django.db.models import fields
from rest_framework import serializers
from .models import *
from courses.models import *



class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = subjects
        fields = '__all__'
        Depth = 3

class Profile_PIC(serializers.ModelSerializer):
    class Meta:
        model=student_profile
        fields=[
            'image',
        ]        

class Profile_Update(serializers.ModelSerializer):
    class Meta:
        model=student_profile
        fields=[
            "student_name",
            "email",
            "address",
            "city",
            "state",
            "pin_code",
            "coaching_name",
            "coaching_city",
            "course_program",
            "date_of_birth",
        ]                        

class StudentStudy(serializers.ModelSerializer):
    class Meta:
        model = student_study
        fields = '__all__'