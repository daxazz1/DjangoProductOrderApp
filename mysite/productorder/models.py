from django.db import models

class Customer(models.Model):
    f_name = models.CharField('First name', max_length=200)
    l_name = models.CharField('Last name', max_length=200)
    email = models.CharField('Email', max_length=200)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

class Order(models.Model):
    customer_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    date = models.DateField('Date', null=True, blank=True)

    ORDER_STATUS = (('e', 'Entered'),('w', 'Waiting'),('p', 'In progress'),('c', 'Completed'),)
    status = models.CharField(max_length=1, choices=ORDER_STATUS, blank=True, default='e', help_text='Status',)

    # def __str__(self):
    #     return {self.customer_id}

class Product_order(models.Model):
    order_id = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField('Quantity')

    @property
    def suma(self):
        return self.quantity * self.product_id.price

    # def __str__(self):
    #     return f"{self.product_id}"



class Product(models.Model):
    name = models.CharField('Name', max_length=200)
    price = models.FloatField('Price')

    def __str__(self):
        return f"{self.name}"


