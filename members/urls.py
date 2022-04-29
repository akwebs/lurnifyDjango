

from django.urls import path , include
from .views import *


app_name = "members"

urlpatterns =[
    
        path('member-home/',member_home,name='member-home'),
        
        #login Process
        path('member-login/',login_view,name='member-login'),
        path('check-member-phone/', check_member_phone , name='check-member-phone'),
        path('check_member_otp/', check_member_otp , name='check_member_otp'),
        path('member-register/',register,name='member-register'),
        path('get-fields/',get_fields,name='get-fields'),
        path('logout/',logout,name='logout'),
        path('profile/',profile,name='profile'),
]
