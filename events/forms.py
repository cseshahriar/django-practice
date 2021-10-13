from django import forms
from events.models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('name', 'description', 'starts_at', 'ends_at')