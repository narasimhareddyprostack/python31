from django import forms 

from userapp.models import User

class UserRegForm(forms.Form):
    name=forms.CharField() 
    email=forms.CharField()
    mobile=forms.IntegerField()

""" class UserRegForm(forms.ModelForm):
    model=User 
    fields="__all__"

    
    class Meta:
         model = UserRegForm  """