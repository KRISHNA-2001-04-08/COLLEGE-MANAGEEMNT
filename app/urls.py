
from django.urls import path
from .import views

urlpatterns = [
    path("",views.intro,name="intro"),
    path("user/",views.user,name="user"),
    path("admin_login/",views.admin_login,name="admin"),
    path("head/",views.head,name="head"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("details/",views.details,name="details"),
    path("admin_details/",views.admin_details,name="admin_details"),
    path("ECE/",views.ECE,name='ECE'),
    path("EEE/",views.EEE,name='EEE'),
    path("CSE/",views.CSE,name='CSE'),
    
]