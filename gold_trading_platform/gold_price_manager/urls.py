from django.urls import path, include
from . import views

urlpatterns = [
    path('gold_rate', views.get_gold_rate, name="gold-rate"),
    path('', include('order_manager.urls')),
]

