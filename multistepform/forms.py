from django import forms
from django.core.exceptions import ValidationError

from .models import MultiStepFormModel


class MultiStepFormModelForm(forms.ModelForm):

    class Meta:
        model = MultiStepFormModel
        fields = ('first_name', 'last_name', 'username', 'password')