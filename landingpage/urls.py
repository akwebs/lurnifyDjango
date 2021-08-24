from . import views
from django.urls import path

app_name = 'landingpage'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
]