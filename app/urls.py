
from django.urls import path
from .import views

urlpatterns = [
    path("",views.intro,name="intro"),
    path("user/",views.user,name="user")
]