from django import forms
from .models import Bank

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Bank
        fields = ('payor', 'payee', 'amount')
