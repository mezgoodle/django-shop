from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import *
from .forms import EmailProductForm
from .utils import cartData, guestOrder
import json
import datetime


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    template_name = 'store/store.html'
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, template_name, context)


def view(request, product_id):
    data = cartData(request)
    cartItems = data['cartItems']

    product = get_object_or_404(Product, id=product_id)
    context = {'product': product, 'cartItems': cartItems}
    template_name = 'store/view.html'
    return render(request, template_name, context)


def share(request, product_id):
    data = cartData(request)
    cartItems = data['cartItems']

    product = get_object_or_404(Product, id=product_id)
    
    sent = False
    if request.method == 'POST':
        form = EmailProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            product_url = request.build_absolute_uri(product.get_absolute_url())
            subject = f"{cd['name']} recommends you read {product.name}"
            message = f"Read {product.name} at {product_url}\n\n {cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, cd['email'], [cd['to']])
            sent = True
    else:
        form = EmailProductForm()

    context = {'product': product, 'cartItems': cartItems, 'form': form, 'sent': sent}
    template_name = 'store/share.html'
    return render(request, template_name, context)


def cart(request):
    template_name = 'store/cart.html'

    data = cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    order = data['order']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, template_name, context)


def checkout(request):
    template_name = 'store/checkout.html'

    data = cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    order = data['order']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, template_name, context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)
    
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )
    return JsonResponse('Payment complete', safe=False)
