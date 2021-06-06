from django.forms import ModelForm
from django import forms
from .models import EventCategory, Event, EventBook,Feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EventCategoryForm(ModelForm):
    class Meta:
        model = EventCategory
        fields = '__all__'


class EventCreationFrom(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'time': forms.TextInput(attrs={"type": "time"}),
            'date': forms.TextInput(attrs={"type": "date"})
        }


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class EventBookingForm(forms.Form):
    event = forms.ModelChoiceField(Event.objects,required=False)
    user = forms.CharField()
    no_of_tickets = forms.IntegerField()
    mobile_number = forms.CharField(max_length=12)



class Feedbackform(ModelForm):
    class Meta:
        model=Feedback
        fields='__all__'
        widgets = {
            'feedback': forms.TextInput(attrs={"class": "feedbackinput"}),

        }
