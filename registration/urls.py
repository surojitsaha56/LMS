from django.urls import path, include
from . import views


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('menu', views.menu, name='menu'),
    path('addstudent', views.addStudent, name='addstudent'),
    path('addbook', views.addBook, name='addbook'),
    path('studenttable', views.studentTable, name='studenttable'),
    path('booktable', views.bookTable, name='booktable'),
    path('issuetable', views.issueTable, name='issuetable'),
    path('showissuetable', views.showIssueTable, name='showissuetable'),
    path('returnbook', views.returnBook, name='returnbook'),
    path('showreturnbook', views.showReturnBook, name='showreturnbook'),
    path('exportexcelstudent', views.exportExcelStudent, name='exportexcelstudent'),
    path('exportexcelbook', views.exportExcelBook, name='exportexcelbook'),
    path('exportexcelbook', views.exportExcelBook, name='exportexcelbook'),
    path('exportexcelissuebook', views.exportExcelIssueBook, name='exportexcelissuebook'),
    path('exportexcelreturnbook', views.exportExcelReturnBook, name='exportexcelreturnbook'),
]

