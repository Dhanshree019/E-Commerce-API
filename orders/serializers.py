from rest_framework.serializers import ModelSerializer
from orders.models import *
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"