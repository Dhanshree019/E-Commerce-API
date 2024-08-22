from django.urls import path
from orders.views import *

urlpatterns = [
    path('orders', OrderView.as_view()),
    path('orders/<int:id>', GetOrderView.as_view()),

    
]