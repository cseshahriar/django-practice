from django import forms
from .models import Image


class ImageCropForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['file']