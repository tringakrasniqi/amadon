from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('order', views.order),
    path('checkout/<int:order_id>', views.checkout)
]