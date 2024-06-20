from django import forms
from .models import *
from django.forms.widgets import NumberInput, TextInput, Textarea, Widget

class TaskTemplateForm(forms.ModelForm):
    class Meta:
        model = TaskTemplates
        fields = 'task', 'template'
        widgets = {
            'task': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
            'template': forms.Select(attrs={'class': 'form-control', 'cols': 200, 'rows': 2}),
        }