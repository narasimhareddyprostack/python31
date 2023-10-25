from django.shortcuts import render

# Create your views here.

def indexPage(request):
    return render(request,'userapp/index.html')

def detailPage(request):
    return render(request,'userapp/details.html')

def contactPage(request):
    return render(request,'userapp/contact.html')