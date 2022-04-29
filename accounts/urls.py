from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


app_name = 'accounts'

urlpatterns =[
            path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
            path('api/user-login/', user_login, name='user-login'),
            path('api/check-user/',check_user , name='check-user'),
            path('api/user-entry/', user_entry , name="user-entry" ),
            path('api/get-streams/', get_streams, name="get-streams"),
            path('api/get-courses/', get_courses , name="get-courses" ),
            ]