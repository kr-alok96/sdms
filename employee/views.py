from django.shortcuts import render
from employee.models import Employee

# Create your views here.
def employee_management(request):
    
    html_data = {'emp_id':'','title':'Employee Management'}
    if request.method == 'POST':
        emp_id = request.POST.get('employee_id')
        emp_name = request.POST.get('employee_name')
        
        newEmployeeData = Employee(employee_id = emp_id,employee_name = emp_name)
        newEmployeeData.save()

        html_data['emp_id'] = emp_id

    return render(request,"employee-management.html",html_data)