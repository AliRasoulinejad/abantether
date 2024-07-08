from decimal import Decimal

from django.core.exceptions import ValidationError
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
        # TODO: it should handle in a good way to return 4xx error instead of 500
        raise ValidationError(code="required_balance", message="increase your account balance")
    Wallet.objects.filter(id=wallet.pk).update(balance=F('balance') - amount)
    Transaction.objects.create(wallet=wallet, value=-amount)


def wallet_check_balance_to_buy(*, wallet: Wallet, amount: Decimal):
    return wallet.balance > amount
