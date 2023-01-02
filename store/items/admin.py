from django.contrib import admin

# Register your models here.
from .models import Glasses, Order

admin.site.register(Glasses)
admin.site.register(Order)
