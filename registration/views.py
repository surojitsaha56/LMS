from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date
import datetime
import xlwt

from .forms import *
from .models import *


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
    auth.logout(request)
    return redirect('/')

@login_required
def menu(request):
    return render(request, 'registration/menu.html')


#Add Student
@login_required
def addStudent(request):
    form=StudentForm()

    if request.method=='POST':
        studentid=request.POST.get('sid')
        dob=request.POST.get('dob')
        print(dob)
        form=StudentForm(request.POST)
        if form.is_valid():
            if not AddStudent.objects.filter(sid=studentid).exists():
                form.save()
                messages.success(request, 'Student was added')
    context={'form': form}
    return render(request, 'registration/addstudent.html', context)

#Add Book
@login_required
def addBook(request):
    form=BookForm()

    if request.method=='POST':
        bookid=request.POST.get('bid')
        form=BookForm(request.POST)
        if form.is_valid():
            if not AddBook.objects.filter(bid=bookid).exists():
                form.save()
                messages.success(request, 'Book was added')
    context={'form': form}
    return render(request, 'registration/addbook.html', context)



#View Student table
@login_required
def studentTable(request):
    students=AddStudent.objects.all()

    return render(request, 'registration/studenttable.html', {'students': students})

#View Book table
@login_required
def bookTable(request):
    books=AddBook.objects.all()
    return render(request, 'registration/booktable.html', {'books': books})

#issue table
@login_required
def issueTable(request):
    form=IssueForm()
    if request.method=='POST':
        studentid=request.POST.get('s_id')
        bookid=request.POST.get('b_id')
        dateOfissue=request.POST.get('dateofissue')
        if AddStudent.objects.filter(sid=studentid).exists() and AddBook.objects.filter(bid=bookid).exists():
            studentname=request.POST.get('s_name')
            bookname=request.POST.get('b_name')
            if str(AddStudent.objects.get(sid=studentid))==studentname and str(AddBook.objects.get(bid=bookid))==bookname:
                form=IssueForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Book issued')
    context={'form': form}
    return render(request, 'registration/issuetable.html', context)

#View Book table
@login_required
def showIssueTable(request):
    issuebooks=IssueBook.objects.all()
    return render(request, 'registration/showissuetable.html', {'issuebooks': issuebooks})


#Return Book form
@login_required
def returnBook(request):
    form=ReturnForm()

    if request.method=='POST':
        studentid2=request.POST.get('sid2')
        bookid2=request.POST.get('bid2')

        if IssueBook.objects.filter(s_id=studentid2).exists() and IssueBook.objects.filter(b_id=bookid2).exists():

            form=ReturnForm(request.POST)
            if form.is_valid():

                tuple2delete=IssueBook.objects.get(s_id=studentid2, b_id=bookid2)

                #fine feature
                DATEOFISSUE=str(tuple2delete.dateofissue)
                DATEOFRETURN=request.POST.get('dateofreturn')
                iyear=int(DATEOFISSUE[0:4])
                imonth=int(DATEOFISSUE[5:7])
                iday=int(DATEOFISSUE[8:10])
                ryear=int(DATEOFRETURN[0:4])
                rmonth=int(DATEOFRETURN[5:7])
                rday=int(DATEOFRETURN[8:10])
                date_1=date(year=iyear, month=imonth, day=iday)
                date_2=date(year=ryear, month=rmonth, day=rday)
                date_delta=date_2-date_1
                number_of_days=date_delta.days
                print(number_of_days)
                fine2pay=0
                if number_of_days>7:
                    fine2pay=(number_of_days-7)*2
                else:
                    fine2pay=0
                print(fine2pay)
                finalform=form.save(commit=False)
                finalform.fine=fine2pay
                messages.success(request, 'Book returned')
                finalform.save()
                
                #delete entry from issuetable
                tuple2delete.delete()
    context={'form': form}
    return render(request, 'registration/returnbook.html', context)

#Show return book
@login_required
def showReturnBook(request):
    returnbooks=ReturnBook.objects.all()
    return render(request, 'registration/showreturnbook.html', {'returnbooks': returnbooks})

#ExportExcelSheet
def exportExcel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Students'+ \
        str(datetime.datetime.now())+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Students')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['ID', 'Name', 'Date of Birth', 'Branch', 'Year']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style=xlwt.XFStyle()

    rows=AddStudent.objects.all().values_list('sid', 'sname', 'dob', 'branch', 'year')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response



