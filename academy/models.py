from django.conf import settings
from django.db import models
from django.utils import timezone


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)


class Lecturer(models.Model):
    lecturer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=100)
    student = models.ManyToManyField(Student)
    teacher = models.OneToOneField(Lecturer, on_delete=models.CASCADE)
