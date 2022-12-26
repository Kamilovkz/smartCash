from django.db import models

# Create your models here.
class Stock(models.Model):
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)
    item_model_number = models.CharField(max_length=100)
    item_country = models.CharField(max_length=100)
    item_buying_date = models.DateField()
    item_cost = models.CharField(max_length=100)
    item_quantity = models.IntegerField(null=False, default=0)

class Product(models.Model):
    name = models.ForeignKey(Stock, on_delete=models.CASCADE)
    selling_date = models.DateField(null=True, blank=True)
    selling_price = models.CharField(max_length=100)
    

