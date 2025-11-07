from django.shortcuts import render


# Create your views here.
def intro(request):
    return render(request,'intro.html')
def user(request):
    return render(request,"user.html")