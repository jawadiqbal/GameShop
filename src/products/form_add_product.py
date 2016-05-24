from django import forms
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "image",
            "developer",
            "publisher",
            "price",
            "category",
            "quantity",
        ]

class CronForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "add_keys"
        ]

    game = forms.ModelChoiceField(queryset=Product.objects.all().order_by('title'))
