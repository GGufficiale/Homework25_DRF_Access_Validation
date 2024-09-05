from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses_lessons.urls'), name='courses'),
    path('users/', include('users.urls'), name='users'),
]
