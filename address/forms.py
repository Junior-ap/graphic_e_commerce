from django import forms
from .models import Address

class AddressCreationForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['cep', 'state', 'city', 'neighborhood', 'street', 'number']
