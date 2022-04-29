from rest_framework import serializers
from .models import *



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = questions_bank
        exclude = ('created_by','updated_by','created_at','updated_at','create_test')
     
class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = instructions
        exclude = ('created_by','updated_by','created_at','updated_at','create_test')