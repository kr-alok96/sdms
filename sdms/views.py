from django.http import HttpResponse
from django.shortcuts import render
from students.models import Student

def home(request):
    html_data = {
        'title':'Home',
    }
    return render(request,'home.html',html_data)

def about_us(request):
    html_data = {
        'title':'About Us',
    }
    return render(request,"about_us.html",html_data)

def about_us_description(request,stakeholder):
    return HttpResponse("Welcome To SDMS "+stakeholder)

def student_management(request):

    html_data = {
        'title': 'Student Management'
    }
    student_data = Student.objects.all()
    html_data['Students'] = student_data # html template expects data in dictionary format

    return render(request,"student_management.html",html_data)
