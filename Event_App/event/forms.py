from django.forms import forms, ModelForm
from event.models import EventCategory, Event, EventBook
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EventCategoryForm(ModelForm):
    class Meta:
        model = EventCategory
        fields = '__all__'


class EventCreationFrom(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class EventBookingForm(ModelForm):
    class Meta:
        model=EventBook
        fields=['event','user','number_of_tickets','Mobile_number','status']
