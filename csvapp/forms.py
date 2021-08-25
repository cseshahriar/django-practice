from django import forms
from .models import CsvModel, Sale

class CsvModelForm(forms.ModelForm):
    class Meta:
        model = CsvModel
        fields = ('file_name',)