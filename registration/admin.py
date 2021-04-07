from django.contrib import admin

# Register your models here.

from .models import AddStudent, AddBook

admin.site.register(AddStudent)
admin.site.register(AddBook)