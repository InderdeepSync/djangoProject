from functools import reduce

from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

User = get_user_model()

class CartManager(models.Manager):
    def obtain_user_cart(self, user):
        if not user.is_authenticated:
            raise Exception("Invalid Operation: Carts are only managed for logged-in users")

        qs = self.get_queryset().filter(user=user)
        return qs.first()

    def new(self, user=None):
        return self.model.objects.create(user=user)

class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products    = models.ManyToManyField(Product, blank=True)

    objects = CartManager()

    @property
    def total(self):
        return reduce(lambda acc, cur: acc + cur, map(lambda p: p.price, self.products.all()), 0)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return "Cart(id={}, user={})".format(self.pk, self.user)
