from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>Index Page</h1>') 


def contact(request):
    return HttpResponse('<h1>Contact Page</h1>')


def service(request):
    return HttpResponse('<h1>Service  Page</h1>')
