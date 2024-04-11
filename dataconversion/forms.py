from django import forms
from .models import Csv, csv_client

class CsvForm(forms.ModelForm):
    
    class Meta:
        model = Csv
        fields = ('file_name',)

class ClientCSVForm(forms.ModelForm):
    class Meta:
        model = csv_client
        fields = '__all__'
        widgets = {
            'CLIENTNUMBER' : forms.TextInput(attrs={'class': 'form-control'}),
            'EntityType' : forms.Select(attrs={'class': 'form-control', 'cols' : 200, 'rows': 2}),
            'ClientName' : forms.TextInput(attrs={'class': 'form-control'}),
            'UnitDescription' : forms.TextInput(attrs={'class': 'form-control'}),
            'Street' : forms.TextInput(attrs={'class': 'form-control'}),
            'City' : forms.TextInput(attrs={'class': 'form-control'}),
            'State_Prov' : forms.TextInput(attrs={'class': 'form-control'}),
            'Country' : forms.TextInput(attrs={'class': 'form-control'}),
            'Fax_Number' : forms.TextInput(attrs={'class': 'form-control'}),
            'EMail' : forms.TextInput(attrs={'class': 'form-control'}),
            'URL' : forms.TextInput(attrs={'class': 'form-control'}),
            'Zip_Code' : forms.TextInput(attrs={'class': 'form-control'}),
            'Telephone_Number' : forms.TextInput(attrs={'class': 'form-control'}),
            'CountryCode' : forms.Select(attrs={'class': 'form-control', 'cols' : 200, 'rows': 2}),
            'Industry' : forms.Select(attrs={'class': 'form-control', 'cols' : 200, 'rows': 2}),
            'ClientType' : forms.Select(attrs={'class': 'form-control', 'cols' : 200, 'rows': 2}),
            'AccountOfficer' : forms.TextInput(attrs={'class': 'form-control'}),
            'ContactPerson' : forms.TextInput(attrs={'class': 'form-control'}),
        }

FORMAT_CHOICES = (
    ('xls', 'xls'),
    ('csv', 'csv'),
    ('jason', 'jason'),
)
class formatforms(forms.Form):
    format = forms.ChoiceField(choices= FORMAT_CHOICES, widget=forms.Select(attrs={'class':'form-select'}))
