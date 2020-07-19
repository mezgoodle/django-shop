from django.contrib import admin
from .models import *

admin.site.site_header = "Store Admin"
admin.site.site_title = "Store Admin Area"
admin.site.index_title = "Welcome to the Shop admin area"

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')
    list_filter = ('name',)
    list_editable = ('email',)
    search_fields = ('name', 'email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_orderd', 'transaction_id')
    list_filter = ('customer',)
    search_fields = ('customer',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added')
    list_filter = ('product',)
    search_fields = ('product', 'order')

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'address', 'city')
    list_filter = ('city', 'customer')
    search_fields = ('customer', 'city')
