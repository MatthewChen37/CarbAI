from django.db import models

# Create your models here.
class Employee(models.Model):
    food_consumed = models.CharField(max_length=100)
    driving_time = models.DecimalField(max_digits=5, decimal_places=2)
    at_home = models.BooleanField()

