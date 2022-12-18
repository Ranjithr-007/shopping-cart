from django.db import models
from django.contrib.auth.models import User, auth
from django.db.models.base import Model

class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.BigIntegerField()