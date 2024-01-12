from django.http import HttpResponse
from django.shortcuts import render
from students.models import Student

def home(request):
    html_data = {
        'title':'Home',
        'clist':[1,2,3]
    }
    return render(request,'home.html',html_data)

def about_us(request):
    return render(request,"about_us.html")

def about_us_description(request,stakeholder):
    return HttpResponse("Welcome To SDMS "+stakeholder)

def student_management(request):

    student_data = Student.objects.all()
    data_dictionary = {'Students':student_data} # html template expects data in dictionary format

    return render(request,"student_management.html",data_dictionary)
