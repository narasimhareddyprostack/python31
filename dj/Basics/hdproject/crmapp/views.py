from django.shortcuts import render
from crmapp.models import Employee
# Create your views here.
def display_Employees(request):
    #get the employee
    emp_list = Employee.objects.all()
    print(emp_list)
    my_emp = {'emp_list':emp_list}
    return render(request,'employee.html', context=my_emp)