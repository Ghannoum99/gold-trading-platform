from django.urls import path, include
from . import views


urlpatterns = [
    path('add-to-cart', views.add_to_cart, name="add-to-cart"),
]

