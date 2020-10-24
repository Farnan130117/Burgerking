from django.db import models
from burgerkingapp.models import Product


class Order(models.Model):
    customer_name   = models.CharField(max_length=50)
    customer_mobile = models.CharField(max_length=50)
    email           = models.EmailField()
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    paid            = models.BooleanField(default=True)
    deposit_amount  = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    return_amount   = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    paid_amount     = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    discount        = models.PositiveIntegerField(default=0) 
    

    def __str__(self):
        return str(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
