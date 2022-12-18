from django.db import models

from django.contrib.auth.models import User

class Products(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.SmallIntegerField()
    status = models.BooleanField()
    Image = models.ImageField()