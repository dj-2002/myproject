from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('cart.html',views.cart,name='cart'),
    path('checkout.html',views.checkout,name='checkout'),
    path('shop.html',views.shop,name='shop'),
    path('single-product.html',views.single,name='single-product'),
    ]