from django.urls import path
from . import views

urlpatterns = [
    path('gold_rate', views.get_gold_rate, name="gold-rate")
]

