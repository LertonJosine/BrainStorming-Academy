from django.urls import path
from .views import signup, notallowed

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("notallowed", notallowed, name="notallowed"),
]
