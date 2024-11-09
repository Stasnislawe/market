from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('addcart/product/<int:pk>', views.cart_add, name='cart_add'),
    path('remove/product/<int:pk>', views.cart_remove, name='cart_remove'),
]