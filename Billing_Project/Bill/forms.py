from django import forms
from django.forms import ModelForm
from Bill.models import Order


class OrderCreationForm(ModelForm):
    class Meta:
        model=Order
        fields=["bill_number","customer_name","phone_number"]