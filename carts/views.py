from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Cart
from products.models import Product

@login_required()
def cart_view(request: HttpRequest):
    cart_object = Cart.objects.obtain_user_cart(user=request.user)
    return render(request, "carts/cart.html", {"cart": cart_object, "cart_products": cart_object.products.all()})


@login_required()
def add_product_to_cart(request):
    product_slug = request.GET.get("product_slug")
    product = Product.objects.filter(slug=product_slug).first()

    cart = Cart.objects.obtain_user_cart(request.user)

    cart.products.add(product)
    return JsonResponse({"message": "Product Added successfully to cart"})


@login_required()
def remove_product_from_cart(request):
    product_slug = request.GET.get("product_slug")
    product = Product.objects.filter(slug=product_slug).first()

    cart = Cart.objects.obtain_user_cart(request.user)

    cart.products.remove(product)
    return JsonResponse({"message": "Product Removed successfully from cart"})
