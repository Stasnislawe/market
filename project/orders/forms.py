from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Field
from django import forms
from .models import Order, OrderWithoutDelivery


class OrderCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # self.helper = FormHelper()
        # self.helper.form_id = 'id-authorForm'
        # self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-lg-3'
        # self.helper.field_class = 'col-lg-10'
        # self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].label = 'Номер телефона'
        self.fields['address'].label = "Адрес - 'нажмите на карту заполниться авто' "
        self.fields['distance'].label = 'Расстояние'
        self.fields['delivery_price'].label = 'Стоимость доставки'
        self.fields['address'].widget.attrs['readonly'] = True
        self.fields['distance'].widget.attrs['readonly'] = True
        self.fields['delivery_price'].widget.attrs['readonly'] = True

    class Meta:
        model = Order
        fields = ['phone_number', 'address', 'delivery_price', 'distance']


class WithoutDeliveryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(WithoutDeliveryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['phone_number'].label = 'Номер телефона'
        # # self.helper.form_id = 'id-authorForm'
        # self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-lg-3'
        # self.helper.field_class = 'col-lg-10'
        # self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'

    class Meta:
        model = OrderWithoutDelivery
        fields = ['phone_number']