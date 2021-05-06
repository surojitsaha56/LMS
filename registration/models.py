from django.db import models

# Create your models here.


class AddStudent(models.Model):
    BRANCH_CHOICES = (
    ('CSE','CSE'),
    ('IT', 'IT'),
    ('EXTC','EXTC'),
    ('Chemical','CHEMICAL'),
    ('Mechanical','MECHANICAL'),
)
    YEAR_CHOICES=(
        ('FE', 'FE'),
        ('SE', 'SE'),
        ('TE', 'TE'),
        ('BE', 'BE'),
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

class IssueBook(models.Model):
    s_id=models.IntegerField()
    s_name=models.CharField(max_length=50)
    b_id=models.IntegerField()
    b_name=models.CharField(max_length=50)
    dateofissue=models.DateField()

    def __str__(self):
        return "Issue "+self.b_name

class ReturnBook(models.Model):
    sid2=models.IntegerField()
    bid2=models.IntegerField()
    dateofreturn=models.DateField()
    fine=models.IntegerField(default=0)

