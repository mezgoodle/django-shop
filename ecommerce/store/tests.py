from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create()
        Customer.objects.create(
            user=user,
            name='maxim',
            email='mezgoodle@gmail.com'
        )

    def test_content(self):
        customer = Customer.objects.get(id=1)
        self.assertEquals(customer.name, 'maxim')
        self.assertEquals(customer.email, 'mezgoodle@gmail.com')

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            name='headphones',
            price=12.236,
            digital=False,
        )

    def test_content(self):
        product = Product.objects.get(id=1)
        self.assertEquals(product.name, 'headphones')
        self.assertEquals(float(product.price), 12.24)
        self.assertEquals(product.digital, False)

class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create()
        Customer.objects.create(
            user=user,
            name='maxim',
            email='mezgoodle@gmail.com'
        )
        customer = Customer.objects.get(id=1)

        Order.objects.create(
            customer=customer,
            transaction_id='123456',
        )

    def test_content(self):
        order = Order.objects.get(id=1)
        self.assertEquals(order.transaction_id, '123456')
        self.assertEquals(order.complete, False)
        self.assertEquals(order.customer, Customer.objects.get(id=1))

class OrderItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create()
        Customer.objects.create(
            user=user,
            name='maxim',
            email='mezgoodle@gmail.com'
        )
        customer = Customer.objects.get(id=1)
        Order.objects.create(
            customer=customer,
            transaction_id='123456',
        )
        order = Order.objects.get(id=1)
        Product.objects.create(
            name='headphones',
            price=12.231,
            digital=False,
        )
        product = Product.objects.get(id=1)

        OrderItem.objects.create(
            order=order,
            product=product,
        )

    def test_content(self):
        orderitem = OrderItem.objects.get(id=1)
        self.assertEquals(orderitem.order, Order.objects.get(id=1))
        self.assertEquals(orderitem.product, Product.objects.get(id=1))
        self.assertEquals(orderitem.quantity, 0)

class ShippingAddressModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create()
        Customer.objects.create(
            user=user,
            name='maxim',
            email='mezgoodle@gmail.com'
        )
        customer = Customer.objects.get(id=1)
        Order.objects.create(
            customer=customer,
            transaction_id='123456',
        )
        order = Order.objects.get(id=1)

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address='Old Trafford, Stretford',
            city='Manchester',
            zipcode='12345',
        )

    def test_content(self):
        shippingaddress = ShippingAddress.objects.get(id=1)
        self.assertEquals(shippingaddress.order, Order.objects.get(id=1))
        self.assertEquals(shippingaddress.customer, Customer.objects.get(id=1))
        self.assertEquals(shippingaddress.address, 'Old Trafford, Stretford')
        self.assertEquals(shippingaddress.city, 'Manchester')
        self.assertEquals(shippingaddress.zipcode, '12345')
        self.assertEquals(shippingaddress.state, None)
