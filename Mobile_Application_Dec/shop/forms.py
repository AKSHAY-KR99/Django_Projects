from django import forms
from django.forms import ModelForm
from shop.models import Brands,Order,Mobile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BrandCreateForm(ModelForm):
    class Meta:
        model=Brands
        fields='__all__'



class MobileCreateForm(ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'


class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']


class OrderForm(ModelForm):
    # product=forms.CharField(max_length=100)
    class Meta:
        model=Order
        fields='__all__'
        widgets={
            "product":forms.TextInput(attrs={"class":"form-control"}),
            "deliveryAddress": forms.TextInput(attrs={"class": "form-control"}),
            "user": forms.TextInput(attrs={"class": "form-control"}),
            'status':forms.
            # "status": forms.TextInput(attrs={"class": "form-control"})
            }