""" Create your models here. """

import uuid
from django.db import models

# Create your models here.

class User(models.Model):
    """" A class for dummy-trading users """
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        editable=False)
    username = models.CharField(max_length=40)
    hash = models.CharField(max_length=60)
    balance = models.DecimalField(default=10000.00, max_digits=8, decimal_places=2)
