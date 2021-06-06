from django import forms
from django.forms import ModelForm
from Bill.models import Order,Purchase
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderCreationForm(ModelForm):
    class Meta:
        model=Order
        fields=["bill_number","customer_name","phone_number"]


class OrderLineForm(forms.Form):
    bill_number=forms.CharField()
    products=Purchase.objects.all().values_list('product__product_name')
    result=[(itemtuple[0],itemtuple[0]) for itemtuple in products]

    product_name=forms.ChoiceField(choices=result)
    product_qty=forms.IntegerField()


class SearchByBillNumber(forms.Form):
    bill_number=forms.CharField(max_length=15)


class SearchByDateForm(forms.Form):
    date=forms.DateField()


class SearchByNameForm(forms.Form):
    customer_name=forms.CharField(max_length=50)



class UserRegForm(UserCreationForm):
    class Mata:
        model=User
        fields=['username','email','password1','password2']


class LoginForm(forms.Form):
    email=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)