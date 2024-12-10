from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.IntegerField()
    phone_number = models.IntegerField()
    age = models.IntegerField()
    house_number = models.CharField(max_length=10)
    zone = models.IntegerField()

# Create your models here.
