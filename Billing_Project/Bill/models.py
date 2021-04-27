from django.db import models

# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=75,unique=True)

    def __str__(self):
        return self.product_name


class Purchase(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=False)
    purchase_price=models.FloatField(null=False)
    selling_price=models.FloatField(null=False)
    purchase_date=models.DateField(auto_now=True)



class Order(models.Model):
    bill_number=models.CharField(max_length=50,unique=True)
    bill_date=models.DateField(auto_now=True)
    customer_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=12)
    bill_total=models.FloatField(default=0,null=True)


    def __str__(self):
        return self.bill_number




class OrderLines(models.Model):
    bill_number=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField()
    amount=models.FloatField()

