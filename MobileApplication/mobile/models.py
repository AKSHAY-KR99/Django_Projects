from django.db import models

# Create your models here.

class Brands(models.Model):
    brand_name=models.CharField(max_length=120)

    def __str__(self):
        return self.brand_name




class Mobile(models.Model):
    mobile_name=models.CharField(max_length=120)
    brand=models.ForeignKey(Brands,on_delete=models.CASCADE)
    price=models.IntegerField(null=False)
    model_name=models.CharField(max_length=120)
    spec=models.CharField(max_length=250)
    description=models.CharField(max_length=120)
    img=models.ImageField(upload_to='images')

    def __str__(self):
        return self.mobile_name
