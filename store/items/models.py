from django.db import models

# Create your models here.
class ItemStock(models.Model):
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)
    item_model_number = models.CharField(max_length=100)
    item_country = models.CharField(max_length=100)
    item_first_price = models.CharField(max_length=100)
    item_buying_date = models.DateField()
    item_count = models.IntegerField()

class ItemSell(models.Model):
    name = models.ForeignKey(ItemStock, on_delete=models.CASCADE)
    selling_date = models.DateField()
    selling_price = models.CharField(max_length=100)
    selling_count = models.IntegerField()
    
    

