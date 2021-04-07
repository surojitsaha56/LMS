from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import AddStudent

class CreateAdminForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']

class LoginForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'password1']


class StudentForm(forms.ModelForm):
    class Meta:
        model = AddStudent
        fields=['sid', 'sname', 'dob', 'branch', 'year']



