from django.shortcuts import render
from .models import Curso
# Create your views here.

def homepageview(request):
    return render(request, "index.html")


def seecourses(request):
    course = Curso.objects.all()
    context = {
        "courses": course
    }

    return render(request, "courses.html", context)