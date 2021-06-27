from django.db import models
from django.db.models.fields import DecimalField

# Create your models here.
class Employee(models.Model):
    daily_screen_time = models.PositiveIntegerField()
    commute_distance = models.PositiveIntegerField()
    breakfast_food = models.CharField(max_length = 100)
    lunch_food = models.CharField(max_length = 100)
    dinner_food = models.CharField(max_length= 100)
    snack_food = models.CharField(max_length = 100)

    did_you_recycle_aluminum_today = models.BooleanField()
    did_you_recycle_plastic_today = models.BooleanField()
    did_you_recycle_glass_today = models.BooleanField()


class Infrastructure(models.Model):
    natural_gas_bill = models.PositiveIntegerField()
    electricity_gas_bill = models.PositiveIntegerField()
    fuel_oil_bill = models.PositiveIntegerField()
    propane_bill = models.PositiveIntegerField()
    thermostat_delta = models.PositiveIntegerField()
