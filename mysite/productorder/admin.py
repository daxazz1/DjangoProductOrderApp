from django.contrib import admin
from .models import Customer, Order, Product_order, Product


class AdminCustomer(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'email')


class AdminProduct_order(admin.ModelAdmin):
    list_display = ('product_id', 'quantity', 'suma')


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price')


class OrderInline(admin.TabularInline):
    model = Product_order


class AdminOrders(admin.ModelAdmin):
    list_display = ('customer_id', 'date', 'status')
    inlines = [OrderInline, ]


admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrders)
admin.site.register(Product_order, AdminProduct_order)
admin.site.register(Product, AdminProduct)
