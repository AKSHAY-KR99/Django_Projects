from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120,unique=True)
    phone=models.CharField(max_length=12)
    username=models.CharField(max_length=120,unique=True)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name

