from django.urls import path, include
from . import views


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('menu', views.menu, name='menu'),
    path('addstudent', views.addStudent, name='addstudent'),
]