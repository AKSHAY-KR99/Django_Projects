
from .models import Brands,Mobile
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BrandCreateForm(ModelForm):
    class Meta:
        model=Brands
        fields='__all__'

class MobileCreateForm(ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'

class UserRegFrom(UserCreationForm):
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']