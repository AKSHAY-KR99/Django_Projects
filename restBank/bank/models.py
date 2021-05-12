from django.db import models

# Create your models here.
class Bank(models.Model):
    accno=models.IntegerField()
    username=models.CharField(max_length=20)
    balance=models.IntegerField(default=0)

    def __str__(self):
        return self.username
