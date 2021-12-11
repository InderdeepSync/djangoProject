from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, JsonResponse
from django.views.generic import ListView

from carts.models import Cart
from orders.models import Order


@login_required()
def place_order(request: HttpRequest):
    cart_object = Cart.objects.obtain_user_cart(user=request.user)
    order_instance = Order.objects.create_order(request.user, cart_object.products.all())
    cart_object.products.set([])

    return JsonResponse({"message": "Your Order was Successful!", "order_id": order_instance.id})


class OrdersListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_obj = Cart.objects.obtain_user_cart(self.request.user)
        context['cart'] = cart_obj
        context['orders_list'] = context["object_list"].filter(user=self.request.user)

        return context
