from django.shortcuts import render
from django.http import HttpResponse
from academy.models import Student, Lecturer, Group

def index(request):
    return render(request, 'index.html')


def get_students(request):
    students = Student.objects.all().order_by('student_id')
    return render(request, 'students.html', {'students': students})


def get_lecturers(request):
    lecturers = Lecturer.objects.all().order_by('lecturer_id')
    return render(request, 'lecturers.html', {'lecturers': lecturers})


def get_groups(request):
    groups = Group.objects.all().order_by('-group_id')
    return render(request, 'groups.html', {'groups': groups})