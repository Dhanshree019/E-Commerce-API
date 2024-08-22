from django.urls import path
from products.views import *

urlpatterns = [
    path('categories', ProductCategoryView.as_view()),
    path('products', ProductView.as_view()),
    path('<int:id>', GetProductView.as_view()),
    path('<int:id>/reviews', ProductReviewView.as_view()),
    path('reviews/<int:id>', UpadteProductReviewView.as_view()),
    
]