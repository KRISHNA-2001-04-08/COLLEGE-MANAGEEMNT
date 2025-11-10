
from django.urls import path
from .import views

urlpatterns = [
    path("",views.intro,name="intro"),
    path("user/",views.user,name="user"),
    #path("staff/",views.staff,name="staff"),
    path("head/",views.head,name="head"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("create/",views.create,name="create")
]