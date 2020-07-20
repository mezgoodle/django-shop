from django.shortcuts import render
from django.http import JsonResponse
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
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items': items, 'order': order}
    return render(request, template_name, context)


def checkout(request):
    template_name = 'store/checkout.html'
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items': items, 'order': order}
    return render(request, template_name, context)


def updateItem(request):
    return JsonResponse('Item was added', safe=False)
