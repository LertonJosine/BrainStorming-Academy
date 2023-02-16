from django.shortcuts import render
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.urls import reverse
from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            if new_user.user_type == 2:
                if new_user.codico_criacao_teacher == 98765:
                    new_user.save()
                    auth_user = authenticate(username=new_user.username, password=request.POST["password1"])
                    login(request, auth_user)
                    return HttpResponseRedirect(reverse("home"))
                else:
                    return HttpResponseRedirect((reverse("notallowed")))
            else:
                new_user.save()
                auth_user = authenticate(username=new_user.username, password=request.POST["password1"])
                login(request, auth_user)
                return HttpResponseRedirect(reverse("home"))
    context = {
        "form": form
    }

    return render(request, "registration/signup.html", context)



def notallowed(request):
    return render(request, "notallowed.html")


# def create_user_teacher(request):
#     if request.method == 'GET':
#         form = CustomUserCreationForm()
#     else:
#         form = CustomUserChangeForm(data=request.POST)
#         new_user = form.save()
#         auth_user = authenticate()