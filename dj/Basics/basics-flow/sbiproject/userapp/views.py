from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    msg="<h1>Inde Page - Django Web Application</h1>"
    return HttpResponse(msg)
def about(request):
    msg = "<h1>About Page - Django Web Application</h1>"
    return HttpResponse(msg)


def service(request):
    msg = "<h1>services Page - Django Web Application</h1>"
    return HttpResponse(msg)


def product(request):
    msg = "<h1>Product Page - Django Web Application</h1>"
    return HttpResponse(msg)
    return HttpResponse(msg)


def contact(request):
    msg="<h1>Contact Page - Django Web Application</h1>"
    return HttpResponse(msg)
    
