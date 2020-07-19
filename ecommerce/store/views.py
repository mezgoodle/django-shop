from django.shortcuts import render
from .models import *


def store(request):
    template_name = 'store/store.html'
    products = Product.objects.all()
    context = {'products': products}
    return render(request, template_name, context)


def cart(request):
    template_name = 'store/cart.html'
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items}
    return render(request, template_name, context)


def checkout(request):
    template_name = 'store/checkout.html'
    context = {}
    return render(request, template_name, context)
