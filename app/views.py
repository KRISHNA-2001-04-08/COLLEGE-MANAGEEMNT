from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import user_passes_test
from .models import Staff



# ---------------------- BASIC PAGES ----------------------
def intro(request):
    return render(request, 'intro.html')

def user(request):
    return render(request, "user.html")


# ---------------------- LOGIN ----------------------
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        department = request.POST['department']
        year = request.POST['year']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                profile = Staff.objects.get(user=user)
            except Staff.DoesNotExist:
                messages.error(request, "User profile not found.")
                return redirect('user')

            # Check dept & year
            if profile.department == department and profile.year == year:
                auth_login(request, user)
                return redirect('details')  # 👈 redirected to dashboard (details)
            else:
                messages.error(request, "Department or year does not match.")
                return redirect('user')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('user')

    return render(request, 'login.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            auth_login(request, user)
            messages.success(request, f"Welcome, Head {username}!")
            return redirect('admin')
        else:
            messages.error(request, "Invalid admin credentials or not a superuser.")
            return redirect('head')

    return render(request, 'admin.html')  


# ---------------------- SIGNUP (ADMIN ONLY) ----------------------

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        department = request.POST['department']
        year = request.POST['year']
        password = request.POST['password']
        re_password = request.POST['re-password']

        if password != re_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        # Create user + staff profile
        user = User.objects.create_user(username=username, password=password)
        user.save()

        Staff.objects.create(user=user, department=department, year=year)

        messages.success(request, "Staff account created successfully!")
        return redirect('details')

    return render(request, 'signup.html')


# ---------------------- DETAILS (DASHBOARD) ----------------------

def head(request):
    return render(request,"head.html")

def details(request):
    return render(request,"details.html")
def admin_details(request):
    return render(request,"admin_details.html")
def ECE(request):
    return render(request,"ECE.html")
def EEE(request):
    return render(request,"EEE.html")
def CSE(request):
    return render(request,"CSE.html")