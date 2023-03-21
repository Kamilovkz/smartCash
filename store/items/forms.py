from django import forms
from .models import Glasses, Order, Discount_Order

# Form for input data (add glasses)
class GlassesForm(forms.ModelForm):
    class Meta:
        model = Glasses
        fields = ['name', 'type', 'model', 'size', 'country', 'price', 'stock']

# Form for input data (add orders)
class OrdersForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'glasses', 'quantity', 'status']

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount_Order
        fields = ['discount']