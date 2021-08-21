from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('', include('gold_price_manager.urls')),
    path('profile', views.get_profile, name="profile"),
]

