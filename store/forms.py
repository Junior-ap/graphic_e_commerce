from django import forms
from .models import Cart, Order

class OrderCreationdeForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name']

