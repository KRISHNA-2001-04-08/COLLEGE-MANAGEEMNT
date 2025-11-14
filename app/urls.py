
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
    path("CSE_1/",views.CSE_1,name="CSE_1"),
    path("CSE_2/",views.CSE_2,name="CSE_2"),
    path("CSE_3/",views.CSE_3,name="CSE_3"),
    path("CSE_4/",views.CSE_4,name="CSE_4"),
    path("ECE_1/",views.ECE_1,name="ECE_1"),
    path("ECE_2/",views.ECE_2,name="ECE_2"),
    path("ECE_3/",views.ECE_3,name="ECE_3"),
    path("ECE_4/",views.ECE_4,name="ECE_4"),
    path("EEE_1/",views.EEE_1,name="EEE_1"),
    path("EEE_2/",views.EEE_2,name="EEE_2"),
    path("EEE_3/",views.EEE_3,name="EEE_3"),
    path("EEE_4/",views.EEE_4,name="EEE_4")
]
