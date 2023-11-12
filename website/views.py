from django.shortcuts import render
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from .forms import *


def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        number = request.POST.get('number', '')
        rollno = request.POST.get('roll', '')
        student = Student(name=name, number=number, rollno=rollno)
        student.save()
    return render(request, 'pfsd.html')

def pfsd(request):
    return render(request, 'pfsd.html')

def honors(request):
    teams = Team.objects.all()

    context = {
        'teams': teams,
    }
    return render(request, 'honors.html', context)