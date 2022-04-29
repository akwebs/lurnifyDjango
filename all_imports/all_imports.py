import this
from django.shortcuts import render ,redirect
from numpy import double

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
from datetime import datetime, timedelta  ,date
import datetime
import pandas as pd
from time import strptime

import razorpay
from django.conf import settings

from accounts.models import *
from courses.models import *
from members.models import *
from students.models import *
from admin_section.models import *


from students.serializers import *
from accounts.serializers import *