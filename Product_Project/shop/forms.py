
from .models import Brands
from django.forms import ModelForm


class BrandCreateForm(ModelForm):
    class Meta:
        model=Brands
        fields='__all__'