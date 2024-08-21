from django.urls import path
from products.views import *

urlpatterns = [
    path('categories', ProductCategoryView.as_view()),
    path('products', ProductView.as_view()),
    path('<int:id>', GetProductView.as_view()),
    
]