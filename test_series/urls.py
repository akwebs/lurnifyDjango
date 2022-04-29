from django.urls import path , include
from .views import *


app_name = "test_series"

urlpatterns =[
    
    path('api/test-request/',test_request,name='test-request'),
]
