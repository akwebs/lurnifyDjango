from django.urls import path 
from .views import *
from students.payments.payment import *
from students.Profile.profile import student_profile_api , profile_pic , profile_update , registration_completed
app_name = "students"

urlpatterns = [
        path('api/lurnify-home/', lurnify_home , name="lurnify-home"),
        path('api/complete-register/', complete_register, name="complete-register"),
        path('api/update-study-pattern/', update_study_pattern),
        path('api/registration-completed/',registration_completed),
        path('api/course-structure/', course_structure , name="course-structure"),
        path('api/lurnifighter-badges/',all_lurnifighter_badges),
        path('api/challenge-accept/',challenge_accept_view),
        path('api/challenge-accepted/<int:pk>/',challenge_accepted),
        path('api/sync-challenge/<str:pk>/',sync_challenge),
        path('api/trophy-list/',trophy_home),
        path('api/trophy-view/<str:pk>/',trophy_view),
        path('api/monthly-certificate/',monthly_certificate_list),
        # wheel 
        path('api/wheel-item/',spin_wheel_item),
        path('api/daily-challenge-accept/<str:pk>/',daily_challenge_accept),
        
        path('api/student-cash-coupons/',student_cash_coupons),
        path('api/cash-coupon-status/',cash_coupon_status),
        path('api/student-pay-fee/',student_pay_fee),
        path('api/payment-handler/',paymenthandler),
        path('api/student-profile/',student_profile_api),
        path('api/profile-pic-update/',          profile_pic),  
        path('api/profile-update/',              profile_update),

        # sync_sudent_study
        path('api/sync-student-study/' , sync_student_study),

]