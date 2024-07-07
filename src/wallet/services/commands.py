from decimal import Decimal

from django.db import transaction
from django.db.models import F

from wallet.models import Wallet, Transaction


@transaction.atomic
def wallet_charge(*, wallet: Wallet, amount: Decimal):
    Wallet.objects.filter(id=wallet.pk).update(balance=F('balance') + amount)
    Transaction.objects.create(wallet=wallet, value=amount)


@transaction.atomic
def wallet_discharge(*, wallet: Wallet, amount: Decimal):
    if wallet.balance < amount:
        return
    Wallet.objects.filter(id=wallet.pk).update(balance=F('balance') - amount)
    Transaction.objects.create(wallet=wallet, value=-amount)
