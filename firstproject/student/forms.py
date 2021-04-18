

from django import forms



class studentRegistrationForm(forms.Form):
    # name,email,course,phone,username,password
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control box'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control box'}))
    course=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control box'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control box'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control box'}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control box'}))

    def clean(self):
        print("From validation")

class studentLogin(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput())
    def clean(self):
        print("Validation Done")
