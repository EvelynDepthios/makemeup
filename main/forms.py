from django.forms import ModelForm
from main.models import Product
from django import forms

CATEGORY_CHOICES = [
    ('Lip Product', 'Lip Product'),
    ('Eye Product', 'Eye Product'),
    ('Face Product', 'Face Product'),
    ('Body Care', 'Body Care'),
    ('Hair Care', 'Hair Care'),
    ('Fragrance', 'Fragrance'),
]

class CreateProductForm(ModelForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    class Meta:
        model = Product
        fields = ["brand","product_name", "price", "description", "category", "ratings"]
        widgets = {
            'price': forms.TextInput(attrs={'class': 'form-input w-full rounded-r-md border-gray-300'}),
        }
        initial = {
            'price': '',
        }
