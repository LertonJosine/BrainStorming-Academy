from django.shortcuts import render
from .models import Curso
from .forms import CursoForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def homepageview(request):
    return render(request, "index.html")


def seecourses(request):
    course = Curso.objects.all()
    context = {
        "courses": course
    }

    return render(request, "courses.html", context)


def create_course(request):
    form = CursoForm(data=request.POST)
    if request.method == 'POST':
    #     form = CursoForm()
    # else:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    context = {
        "form": form
    }

    return render(request, "create_course.html", context)