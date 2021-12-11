from django.urls import path
from .views import cart_view, add_product_to_cart, remove_product_from_cart

urlpatterns = [
    path('view/', cart_view, name="view"),
    path('add/', add_product_to_cart, name="add"),
    path('remove/', remove_product_from_cart, name="remove")
]