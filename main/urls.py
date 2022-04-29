
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls' , namespace="accounts") ),
    path('', include('admin_section.urls' , namespace="admin_section")),
    path('',include('courses.urls' , namespace="courses") ),
    path('',include('students.urls' , namespace="students") ),
    path('',include('test_series.urls' , namespace="test_series") ),
    path('', include('web_src.urls' , namespace="web_src") ),
    path('', include('members.urls' , namespace="members") ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
