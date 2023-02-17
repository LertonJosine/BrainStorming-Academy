from django.urls import path
from .views import homepageview, seecourses, create_course

urlpatterns = [
    path('', homepageview, name="home"),
    path('courses/', seecourses, name="courses"),
    path("create_course/", create_course, name="create_course")
]