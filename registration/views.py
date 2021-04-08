from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateAdminForm, LoginForm, StudentForm, BookForm


#signup method
def signup(request):
    form=CreateAdminForm()

    if request.method=='POST':
        form=CreateAdminForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created')
    context={'form': form}
    return render(request, 'registration/signup.html', context)

#login method
def loginPage(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'registration/login.html')
    return render(request, 'registration/login.html')

#logout method
def logoutUser(request):
    return redirect('home')

def menu(request):
    logout(request)
    return render(request, 'registration/menu.html')


#Add Student
def addStudent(request):
    form=StudentForm()

    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form': form}
    return render(request, 'registration/addstudent.html', context)

#Add Book
def addBook(request):
    form=BookForm()

    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form': form}
    return render(request, 'registration/addbook.html', context)