from django.db import models


# Create your models here.

class AccountCreation(models.Model):
    accno=models.IntegerField(unique=True)
    username=models.CharField(max_length=50,unique=True)
    account_type=models.CharField(max_length=50,default="savings")
    balance=models.FloatField(default=0)