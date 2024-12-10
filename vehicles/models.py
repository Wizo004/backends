from django.db import models


class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=15)
    model = models.CharField(max_length=10)
    make = models.CharField(max_length=10)

# Create your models here.
