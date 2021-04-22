from django.db import models

# Create your models here.

class Brands(models.Model):
    brand_name=models.CharField(max_length=50)
    def __str__(self):
        return self.brand_name
