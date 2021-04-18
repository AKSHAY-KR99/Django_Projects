from django.contrib import admin
from shop.models import Mobile,Brands,Order
# Register your models here.

admin.site.register(Brands)
admin.site.register(Mobile)
admin.site.register(Order)
