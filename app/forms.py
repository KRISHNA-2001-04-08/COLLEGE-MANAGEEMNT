from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Staff

class SignupForm(UserCreationForm):
    class Meta:
        model = Staff
        fields = ['username', 'department', 'year',  'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = Staff
        fields = ['username','department', 'year', 'password']