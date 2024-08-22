from rest_framework.serializers import ModelSerializer
from products.models import *

class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductReviewSerializer(ModelSerializer):
    class Meta:
        model = ProductReview
        fields = "__all__"
