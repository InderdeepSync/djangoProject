from django.http import Http404

from django.views.generic import ListView, DetailView

from carts.models import Cart
from .models import Product
from django.shortcuts import get_object_or_404


class ProductDetailSlugView(DetailView):
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            cart_obj = Cart.objects.obtain_user_cart(self.request.user)
            context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Product, slug=slug)


class ProductListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            cart_obj = Cart.objects.obtain_user_cart(self.request.user)
            context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        return Product.objects.all()
