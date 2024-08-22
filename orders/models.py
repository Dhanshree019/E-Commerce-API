from django.db import models
from accounts.models import CustomUser
from products.models import Product
# Create your models here.
class Order(models.Model):
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    # status => pending | canceled | shipped | delivered
    status = models.CharField(default="pending",max_length=256)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    
    # timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)


class Payment(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # status => pending | completed | failed
    status = models.CharField(default="pending",max_length=256)

    # timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)