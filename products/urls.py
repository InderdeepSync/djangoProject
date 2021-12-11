from django.contrib import admin
from django.urls import path
from .views import ProductListView, ProductDetailSlugView

app_name = "products"

urlpatterns = [
    path('all/', ProductListView.as_view(), name="all"),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name="detail")
]
