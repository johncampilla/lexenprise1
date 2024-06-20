from django import forms
from django.forms import TextInput, ModelForm, DateTimeInput
from django.db.models.query import QuerySet
from django.forms import widgets
from django.forms.widgets import NumberInput, TextInput, Textarea, Widget
from casefolder.models import Lawyer_Data 
from reference_lookup.models import AppType


class DueDateEntryForm(forms.Form):
    From_date = forms.DateField(label='From Date', widget=NumberInput(attrs={'type': 'date'}))
    To_date = forms.DateField(label='To Date', widget=NumberInput(attrs={'type': 'date'}))
    Lawyer = forms.ModelChoiceField(label='Lawyer', queryset=Lawyer_Data.objects.all())
    AppType = forms.ModelChoiceField(label='AppType', queryset=AppType.objects.all())


