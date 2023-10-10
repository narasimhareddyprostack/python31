from django.shortcuts import render

# Create your views here.

def index(request):
    emp_dict ={'emp_name':'Rahul Gandhi', 'id':101}
    return render(request,'index.html', context=emp_dict)

def about(request):
    
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')
