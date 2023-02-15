from django.urls import path
from .views import homepageview, seecourses

urlpatterns = [
    path('', homepageview, name="home"),
    path('courses/', seecourses, name="courses")
]