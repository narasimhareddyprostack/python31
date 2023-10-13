from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Indes Page")
def login(request):
    return HttpResponse('Login Successfully')
def logout(request):
    return HttpResponse('Logout Successfull')