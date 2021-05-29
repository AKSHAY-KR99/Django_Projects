
from django.forms import ModelForm, forms
from .models import EventCategory, Event


class EventCategoryForm(ModelForm):
    class Meta:
        model=EventCategory
        fields='__all__'

class EventCreationFrom(ModelForm):
    class Meta:
        model=Event
        fields='__all__'
