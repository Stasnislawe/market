from django.shortcuts import render
from .models import OrderItem, OrderItemWD
from .forms import OrderCreateForm, WithoutDeliveryForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid() and cart:
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order/created.html',
                             {'order': order})
        return render(request, 'orders/order/cartisempty.html')
    else:
        if cart:
            form = OrderCreateForm()
            return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
        return render(request, 'orders/order/cartisempty.html')

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


def order_create2(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = WithoutDeliveryForm(request.POST)
        if form.is_valid() and cart:
            order = form.save()
            for item in cart:
                OrderItemWD.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
        return render(request, 'orders/order/cartisempty.html')
    else:
        if cart:
            form = WithoutDeliveryForm()
            return render(request, 'orders/order/createwd.html', {'cart': cart, 'form': form})
        return render(request, 'orders/order/cartisempty.html')

    return render(request, 'orders/order/createwd.html', {'cart': cart, 'form': form})

