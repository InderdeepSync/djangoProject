# from django.contrib.auth.mixins import LoginRequiredMixin
import os

from django.db import models
# LoginRequiredMixin
from django.db.models.signals import pre_save
from django.urls import reverse

from products.utils import unique_slug_generator


def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    _, extension = os.path.splitext(base_name)
    return extension


def upload_image_path(instance, filename):
    extension = get_file_ext(filename)

    final_filename = '{product_slug}{ext}'.format(product_slug=instance.slug, ext=extension)
    return "products/{final_filename}".format(
        final_filename=final_filename
    )


class Product(models.Model):
    title = models.CharField(max_length=128, blank=False, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, blank=False)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    quantity_available = models.IntegerField(blank=False, default=0)

    def get_absolute_url(self):
        # return "/products/{slug}/".format(slug=self.slug)
        return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def __repr__(self):
        return "Product(title={})".format(self.title)


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
