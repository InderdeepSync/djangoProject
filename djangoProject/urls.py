from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic import RedirectView

from orders.views import place_order, OrdersListView
from . import settings
from .views import home_page, UserLoginView, register_view

urlpatterns = [
    path("favicon.ico/", RedirectView.as_view(url='/static/favicon.ico')),
    path("", home_page, name="home"),

    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),

    path("cart/", include('carts.urls')),
    path("products/", include("products.urls", namespace="products")),
    path('place-order/', place_order, name="place-order"),
    path('orders/', OrdersListView.as_view()),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
