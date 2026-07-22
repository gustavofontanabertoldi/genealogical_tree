from django import forms
from .models import Person, Tree, Event, EventParticipant

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            "full_name",
            "sex",
            "birth_date",
            "death_date"
        ]
        widgets = {
            "sex": forms.RadioSelect()
        }

class TreeForm(forms.ModelForm):
    class Meta:
        model = Tree
        fields = [
            "name",
            "description",
        ]

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "event_name",
            "event_type",
            "event_date",
            "event_location",
            "description"
        ]
        widgets = {
            "event_type": forms.Select(),
            "event_date": forms.SelectDateWidget(
                years=range(1500, 2031)
            )
        }

class EventParticipantForEventForm(forms.ModelForm):
    class Meta:
        model = EventParticipant
        fields = [
            "person",
            "role"
        ]

class EventParticipantForPersonForm(forms.ModelForm):
    class Meta:
        model = EventParticipant
        fields = [
            "role",
        ]