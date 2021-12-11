from django.contrib.auth.views import LoginView
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from carts.models import Cart
from .forms import RegisterForm

from django.contrib.auth import get_user_model


User = get_user_model()
def home_page(request: HttpRequest):
    context = {}
    if request.user.is_authenticated:
        cart_obj = Cart.objects.obtain_user_cart(request.user)
        context['cart'] = cart_obj
    return render(request, "home_page.html", context)


class UserLoginView(LoginView):
    template_name = "auth/login-page.html"


def register_view(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username  = form.cleaned_data.get("username")
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        new_user  = User.objects.create_user(username, email, password)
        Cart.objects.new(user=new_user)
        return redirect("login")

    return render(request, "auth/registration-page.html", context)