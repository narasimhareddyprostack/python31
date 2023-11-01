from django.shortcuts import render
from django.shortcuts import redirect

from product.forms import ProductForm

# Create your views here.
def product(request):
    if request.method=="POST":
        form=ProductForm(request.POST)
        form.save()
        return redirect("/display")

    form=ProductForm()
    return render(request, 'index.html',{'form':form})

def display(request):
    #business logic
    return render(request,'display.html')

def updateproduct(request):
    #business logic 
    return render(request, 'create.html')

def deleteproduct(request):
    # business logic
     
    return redirect("/display")