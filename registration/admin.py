from django.contrib import admin

# Register your models here.

from .models import AddStudent, AddBook, IssueBook, ReturnBook

admin.site.register(AddStudent)
admin.site.register(AddBook)
admin.site.register(IssueBook)
admin.site.register(ReturnBook)