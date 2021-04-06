from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateAdminForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']

class LoginForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'password1']

