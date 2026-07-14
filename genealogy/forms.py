from django import forms
from .models import Person

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