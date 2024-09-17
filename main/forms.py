from django.forms import ModelForm
from main.models import Product

class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "ratings"]