from django.shortcuts import render
from empapp.models import Employee,User

# Create your views here.

def display_Employee(request):
    #model logic to fetch employee data
    emp_list=Employee.objects.all()
    my_emp={'emp_list':emp_list}
    return render(request, "emp.html", context=my_emp)

def display_User(request):
    user_list=User.objects.all()
    my_user={'user_list':user_list}
    return render(request, "user.html", context=my_user)