from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'image',
            'price',
            'description',
            'rentor_name',
            'rentor_contact'
        ]