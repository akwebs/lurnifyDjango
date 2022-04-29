
from django.db.models import fields
from rest_framework import serializers
from .models import *



class CHECKUSER(serializers.Serializer):
    phone       = serializers.CharField(max_length=20)
