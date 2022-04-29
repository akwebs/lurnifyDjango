from django.urls import path , include
from .views import *


app_name = "web_src"

urlpatterns =[
    path('', index , name="home"),
    path('base', home , name="base"),
    path('privacy', privacy , name="privacy"),
    path('terms', terms , name="terms"),
    path('refund', refund , name="refund"),
    path('about', about_us , name="about"),
    path('mission',our_mission , name="mission"),
    path('vision',our_vision , name="vision"),
]
