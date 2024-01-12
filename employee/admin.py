from django.contrib import admin

# Register your models here.
from employee.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id','employee_name']

admin.site.register(Employee,EmployeeAdmin)