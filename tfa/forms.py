from .models import Code
from django import forms


class CodeForm(forms.ModelForm):
    number = forms.CharField(label='Code', help_text='Enter SMS verification code.')

    class Meta:
        model = Code
        fields = ('number',)