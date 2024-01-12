from django.shortcuts import render
from employee.models import Employee

# Create your views here.
def employee_management(request):
    emp_id = ''
    data = {'emp_id':''}
    if request.method == 'POST':
        emp_id = request.POST.get('employee_id')
        emp_name = request.POST.get('employee_name')
        
        newEmployeeData = Employee(employee_id = emp_id,employee_name = emp_name)
        newEmployeeData.save()

        data = {'emp_id':emp_id}

    return render(request,"employee-management.html",data)