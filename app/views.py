from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SignupForm, LoginForm
from .models import Staff


# Create your views here.
def intro(request):
    return render(request,'intro.html')
def user(request):
    return render(request,"user.html")

def head(request):
    return render(request,"head.html")

def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")
def create(request):
    return render(request,"create.html")