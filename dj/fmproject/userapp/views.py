from django.shortcuts import render
from . import forms
# Create your views here.

def userRegistrationView(request):
    form=forms.UserRegForm()
    return render(request,'registration.html',{'form':form})



def successView(request):
    if request.method=='POST':
        form=forms.UserRegForm(request.POST)
        if form.is_valid():
            print("Data",form)
            
    return render(request,'success.html')