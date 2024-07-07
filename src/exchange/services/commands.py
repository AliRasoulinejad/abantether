from decimal import Decimal

from django.db import transaction

from coin.models import Coin
from exchange.models import TransactionLog


@transaction.atomic
def buy_from_exchange(*, coin: Coin, amount: Decimal):
    TransactionLog.objects.create(coin=coin, amount=amount)

    # TODO: add buy logic

    return
