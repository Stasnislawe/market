from django import forms
from .models import Order, OrderWithoutDelivery


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'delivery_price', 'distance']


class WithoutDeliveryForm(forms.ModelForm):
    class Meta:
        model = OrderWithoutDelivery
        fields = ['first_name', 'last_name', 'phone_number']