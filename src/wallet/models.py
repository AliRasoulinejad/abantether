from django.db import models

from common.models import BaseModel
from user.models import User


class Wallet(BaseModel):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Transaction(BaseModel):
    wallet = models.ForeignKey(Wallet, on_delete=models.DO_NOTHING, related_name="transactions")
    value = models.DecimalField(max_digits=10, decimal_places=2)
