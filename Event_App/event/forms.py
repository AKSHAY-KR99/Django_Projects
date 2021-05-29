from django.forms import forms,ModelForm
from event.models import EventCategory,Event

class EventCategoryForm(ModelForm):
    class Meta:
        model=EventCategory
        fields='__all__'

class EventCreationFrom(ModelForm):
    class Meta:
        model=Event
        fields='__all__'
