from django.shortcuts import render
from django.views.generic import TemplateView
from orders.models import OrderItem, OrderItemWD

from cart.cart import Cart


# Create your views here.


def profile(request):
    cart = Cart(request)
    orders = OrderItemWD.objects.filter(order__user=request.user.id)
    return render(request, 'sign/profile.html', context={cart: 'cart', orders: 'orders'})


class ProfileView(TemplateView):
    template_name = 'sign/profile.html'

    def get_context_data(self, **kwargs):
        kwargs['cart'] = Cart(self.request)
        kwargs['orders'] = OrderItemWD.objects.filter(order__user=self.request.user)
        return super().get_context_data(**kwargs)