from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse

from carts.models import Cart
from orders.models import Order


@login_required()
def place_order(request: HttpRequest):
    cart_object = Cart.objects.obtain_user_cart(user=request.user)
    order_instance = Order.objects.create_order(request.user, cart_object.products.all())
    cart_object.products.set([])

    return JsonResponse({"message": "Your Order was Successful!", "order_id": order_instance.id})
