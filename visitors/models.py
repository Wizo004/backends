from contextlib import nullcontext

from django.db import models


class Visitor(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    id_number = models.IntegerField()
    vehicle_number = models.CharField(max_length=10,blank=True, null=True)
    vehicle_model = models.CharField(max_length=10, blank=True, null=True)

# Create your models here.
