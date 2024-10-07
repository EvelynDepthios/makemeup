from django.forms import ModelForm
from main.models import Product
from django import forms
from django.utils.html import strip_tags

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
        fields = ["brand","product_name", "description", "category", "price", "ratings"]
        widgets = {
            'price': forms.TextInput(attrs={'class': 'form-input w-full rounded-r-md border-gray-300'}),
        }
        initial = {
            'price': '',
        }
    def clean_brand(self):
        brand = self.cleaned_data["brand"]
        return strip_tags(brand)

    def clean_product_name(self):
        product_name = self.cleaned_data["product_name"]
        return strip_tags(product_name)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
