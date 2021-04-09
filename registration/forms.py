from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import AddStudent, AddBook, IssueBook

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

class BookForm(forms.ModelForm):
    class Meta:
        model = AddBook
        fields=['bid', 'bname', 'isbn', 'author']

class IssueBookForm(forms.ModelForm):
    class Meta:
        model = IssueBook
        fields=['iid', 'sid', 'sname', 'bid', 'bname', 'dateofissue']





