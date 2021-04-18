from django.contrib import admin

# Register your models here.

from .models import Mobile,Brands

admin.site.register(Brands)
admin.site.register(Mobile)
