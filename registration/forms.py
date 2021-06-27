from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import AddStudent, AddBook, IssueBook, ReturnBook

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
        fields=['bid', 'bname', 'isbn', 'author', 'bcount']

class IssueForm(forms.ModelForm):
    class Meta:
        model = IssueBook
        fields=['s_id', 's_name', 'b_id', 'b_name', 'dateofissue']

class ReturnForm(forms.ModelForm):
    class Meta:
        model = ReturnBook
        fields=['sid2', 'bid2', 'dateofreturn']









