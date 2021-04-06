from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateAdminForm, LoginForm

def signup(request):
    form=CreateAdminForm()

    if request.method=='POST':
        form=CreateAdminForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created')
    context={'form': form}
    return render(request, 'registration/signup.html', context)

def loginPage(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
    return render(request, 'registration/login.html')

def logout(request):
    return render('home')

def menu(request):
    return render(request, 'registration/menu.html')

