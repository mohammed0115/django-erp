from django import forms
from Products.models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name','p_type','sale_price',
        'p_cost','serial_number','company','product_created','product_end']
        


