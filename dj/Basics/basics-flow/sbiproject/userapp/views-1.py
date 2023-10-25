from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Index Page")
def about(request):
    return HttpResponse("About US Page")


def service(request):
    return HttpResponse("Services Page")


def product(request):
    return HttpResponse("Product  Page")


def contact(request):
    return HttpResponse("Contact  Page")
