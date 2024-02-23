from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.urls import reverse


# Create your models here.

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, blank=True, related_name="custom_user_group")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="custom_user_permission")
    

class Ingredient(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.FloatField()
    unit=models.CharField(max_length=100)
    cost=models.DecimalField(decimal_places=2,max_digits=10)

class BakeryItem(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    ingredient=models.ManyToManyField('Ingredient')
    cost_price=models.DecimalField(decimal_places=2,max_digits=10)
    selling_price=models.DecimalField(decimal_places=2,max_digits=10)

class Inventory(models.Model):
    item=models.ForeignKey('BakeryItem',on_delete=models.CASCADE)
    quantity=models.IntegerField()

class Order(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.PROTECT)
    items=models.ManyToManyField('BakeryItem')
    total_amount=models.DecimalField(decimal_places=2,max_digits=10)
    status=models.CharField(max_length=100)
    date_ordered=models.DateTimeField()


class Basket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class LineItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='lines')
    product = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cost_price = models.DecimalField(decimal_places=2, max_digits=10)
    selling_price = models.DecimalField(decimal_places=2, max_digits=10)

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)