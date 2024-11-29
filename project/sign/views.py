from django.shortcuts import render
from django.views.generic import TemplateView

from cart.cart import Cart


# Create your views here.


def profile(request):
    cart = Cart(request)
    return render(request, 'sign/profile.html', context={cart: 'cart'})