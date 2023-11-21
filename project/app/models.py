from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.db.models import Avg, ExpressionWrapper, F, DecimalField


class Bottle(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    items = models.ManyToManyField(Bottle, through='OrderItem')
    order_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)


class OrderItem(models.Model):
    bottle = models.ForeignKey(Bottle, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Employee(models.Model):
    name = models.CharField(max_length=255)
    is_busy = models.BooleanField(default=False)


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


class Revenue(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()