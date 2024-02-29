from django.shortcuts import render
from . models import Student
from . models import Teacher
# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def student(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})

def insert_student(request):
    return render(request, 'insert_student.html')





def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {'teachers': teachers})





