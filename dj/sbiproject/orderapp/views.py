from django.shortcuts import render

# Create your views here.


def indexPage(request):
    return render(request, 'orderapp/index.html')


def detailPage(request):
    return render(request, 'orderapp/details.html')
