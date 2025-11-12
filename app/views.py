from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Staff



# Create your views here.
def intro(request):
    return render(request,'intro.html')
def user(request):
    return render(request,"user.html")



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
                
                return redirect('details')
            else:
                messages.error(request, "Department or year does not match.")
                return redirect('user')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('user')

    return render(request, 'user.html')


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

        # Check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        # Create user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect('user')

    return render(request, 'signup.html')

def details(request):
    return render(request,"details.html")