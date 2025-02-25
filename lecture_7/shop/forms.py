from django import forms

from shop.models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ProductForm(forms.ModelForm):
    name = forms.CharField(min_length=1, max_length=200, required=True)
    description = forms.CharField(min_length=0, max_length=2000, required=False)
    amount = forms.IntegerField(min_value=0, max_value=1000, required=True)
    price = forms.IntegerField(min_value=0, required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['name', 'description', 'amount', 'price', 'image']
