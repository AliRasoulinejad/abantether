from django.db import models

from common.models import BaseModel


class Coin(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
