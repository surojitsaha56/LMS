from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from .forms import CreateAdminForm

def signup(request):
    form=CreateAdminForm()

    if request.method=='POST':
        form=CreateAdminForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created')
    context={'form': form}
    return render(request, 'registration/signup.html', context)

def login(request):
    form=UserCreationForm()

    context={'form': form}
    return render(request, 'registration/login.html')

def logout(request):
    return render('home')

def menu(request):
    return render(request, 'registration/menu.html')

