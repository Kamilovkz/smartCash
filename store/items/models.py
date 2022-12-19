from django.db import models

# Create your models here.
class GlassesBuy(models.Model):
    glasses_name = models.CharField(max_length=100)
    glasses_type = models.CharField(max_length=100)
    glasses_model_number = models.CharField(max_length=100)
    glasses_country = models.CharField(max_length=100)
    glasses_first_price = models.CharField(max_length=100)
    glasses_buying_date = models.DateField()

class GlassesSell(models.Model):
    glasses = models.ForeignKey(GlassesBuy, on_delete=models.CASCADE)
    glasses_type = models.CharField(max_length=100)
    glasses_model_number = models.CharField(max_length=100)
    glasses_country = models.CharField(max_length=100)
    glasses_first_price = models.CharField(max_length=100)
    glasses_count = models.IntegerField()

