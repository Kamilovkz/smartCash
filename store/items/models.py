from django.db import models
from django.contrib.auth.models import User


class Glasses(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    glasses = models.ForeignKey(Glasses, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    date_placed = models.DateField(auto_now_add=True)
    discount = models.IntegerField(default=0)
    status = models.CharField(max_length=255, default="confirmed")

    def __str__(self):
        return f"{self.glasses} sold in {self.quantity} quantity by price {self.total_price}$ Date: {self.date_placed}"

    def calculate_total_price(self):
        self.total_price = self.glasses.price * self.quantity

    def update_stock(self, inital_quantity):
        self.glasses.stock += inital_quantity
        self.glasses.stock -= self.quantity
        self.glasses.save()
