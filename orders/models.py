from functools import reduce

from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

User = get_user_model()

class OrderManager(models.Manager):
    def create_order(self, user, products):
        order_obj = self.model.objects.create(user=user)
        order_obj.products.set(products)
        return order_obj

class Order(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products    = models.ManyToManyField(Product, blank=True)

    objects = OrderManager()

    @property
    def total(self):
        return reduce(lambda acc, cur: acc + cur, map(lambda p: p.price, self.products.all()), 0)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return "Order(id={}, user={})".format(self.pk, self.user)
