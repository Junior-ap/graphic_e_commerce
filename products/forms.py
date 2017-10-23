from django import forms
from .models import Product, FactoryItem

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'size', 'description', 'amount', 'saleValue', 'category', 'acquiredValue']
