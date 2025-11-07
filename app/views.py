from django.shortcuts import render


# Create your views here.
def intro(request):
    return render(request,'intro.html')
def user(request):
    return render(request,"user.html")
def staff(request):
    return render(request,"staff.html")
def head(request):
    return render(request,"head.html")