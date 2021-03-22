from django.db import models

# Create your models here.

from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=191)
    phone_no = models.CharField(max_length=12)
    emailid = models.CharField(max_length=20)
    Address = models.CharField(max_length=191)
    grno = models.CharField(max_length=10, primary_key=True, )
    created_on = models.DateTimeField(auto_now_add=True)


class stu_data(models.Model):
    grno = models.CharField(max_length=10, primary_key=True)
    attendence = models.CharField(max_length=40)
    feestatus = models.CharField(max_length=90)
    assin_id = models.CharField(max_length=20, unique=True)
    assin_ls = models.CharField(max_length=130)
    assin_status = models.CharField(max_length=50)
    studentdetails = models.OneToOneField(Student , on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


class teacher_dat(models.Model):
    teacher_fullname = models.CharField(max_length=30)
    teacher_id = models.CharField(max_length=30, primary_key=True)
    subject = models.CharField(max_length=30)

class class_dat(models.Model):
    subject = models.ManyToManyField(teacher_dat)
    subjectcode = models.CharField(max_length=20, default='nil')
    cteacher = models.CharField(max_length=30)


class assinmain(models.Model):
    class_dat   = models.ForeignKey(class_dat, on_delete=models.CASCADE)
    assin_created = models.DateTimeField(auto_created=True)
    assin_due = models.DateTimeField()
    assin_head = models.CharField(max_length=50)
    assin_desc = models.CharField(max_length=300)

class grades_dat(models.Model):
    exam_title= models.CharField(max_length=30)
    exam_grades = models.CharField(max_length=30)