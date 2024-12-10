from django.db import models

class Payment(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.IntegerField()
    phone_number = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_type = models.CharField(max_length=100)
    transaction_code = models.CharField(max_length=100, null=True, blank=True)
# Create your models here.
