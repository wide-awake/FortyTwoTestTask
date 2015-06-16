from django import forms
from django.conf import settings

from .models import Person
from functools import partial


class PersonForm(forms.ModelForm):
    """
    This form only for display & validate model data
    """
    class Meta:
        model = Person
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'datepicker'}),
        }