from django.shortcuts import render
from .models import *


def store(request):
    template_name = 'store/store.html'
    products = Product.objects.all()
    context = {'products': products}
    return render(request, template_name, context)


def cart(request):
    template_name = 'store/cart.html'
    context = {}
    return render(request, template_name, context)


def checkout(request):
    template_name = 'store/checkout.html'
    context = {}
    return render(request, template_name, context)
