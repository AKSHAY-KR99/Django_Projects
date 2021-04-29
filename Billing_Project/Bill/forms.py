from django import forms
from django.forms import ModelForm
from Bill.models import Order,Purchase


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