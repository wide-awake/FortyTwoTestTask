from django import forms

from .models import Person


class PersonForm(forms.ModelForm):
    """
    This form only for display & validate model data
    """
    class Meta:
        model = Person