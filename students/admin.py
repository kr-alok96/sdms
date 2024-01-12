from django.contrib import admin

# Register your models here.
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_admnNo','student_name','student_dob']

admin.site.register(Student,StudentAdmin)