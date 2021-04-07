from django.db import models

# Create your models here.


class AddStudent(models.Model):
    BRANCH_CHOICES = (
    ('cse','CSE'),
    ('it', 'IT'),
    ('extc','EXTC'),
    ('chemical','CHEMICAL'),
    ('mechanical','MECHANICAL'),
)
    YEAR_CHOICES=(
        ('first', 'FE'),
        ('second', 'SE'),
        ('third', 'TE'),
        ('fourth', 'BE'),
    )
    sid=models.IntegerField()
    sname=models.CharField(max_length=50)
    dob=models.DateField()
    branch=models.CharField(max_length=15, choices=BRANCH_CHOICES, default='cse')
    year=models.CharField(max_length=10, choices=YEAR_CHOICES, default='first')

    def __str__(self):
        return self.sname

class AddBook(models.Model):
    bid=models.IntegerField()
    bname=models.CharField(max_length=50)
    isbn=models.CharField(max_length=20)
    author=models.CharField(max_length=50)

    def __str__(self):
        return self.bname
