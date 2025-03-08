from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=300)
    desc=models.CharField(max_length=1000)
    img=models.ImageField(upload_to='product_images/',null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)

class Addcard(models.Model):
    name=models.CharField(max_length=300)
    desc=models.CharField(max_length=1000)
    img=models.ImageField(upload_to='product_images/',null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)  # Quantity field

    def total_cost(self):
        return self.cost * self.quantity

class Buy(models.Model):
    name=models.CharField(max_length=300)
    desc=models.CharField(max_length=1000)
    img=models.ImageField(upload_to='product_images/',null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)