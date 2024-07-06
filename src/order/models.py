from django.db import models

from coin.models import Coin
from common.models import BaseModel
from user.models import User


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    coin = models.ForeignKey(Coin, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
