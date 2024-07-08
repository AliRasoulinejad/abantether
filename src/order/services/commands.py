from decimal import Decimal

from django.conf import settings
from django.db import transaction

from coin.models import Coin
from exchange.services.commands import buy_from_exchange
from order.models import Order
from user.models import User
from wallet.services.commands import wallet_discharge, wallet_check_balance_to_buy

order_list = "orders-{coin}"

# Lua script to handle atomic insert and check
lua_script = """
local sum = 0
local elements = redis.call('LRANGE', KEYS[1], 0, -1)
for _, v in ipairs(elements) do
    sum = sum + tonumber(v)
end
sum = sum + tonumber(ARGV[1])

if sum > tonumber(ARGV[2]) then
    redis.call('DEL', KEYS[1])
    return sum
else
    redis.call('RPUSH', KEYS[1], ARGV[1])
    return 0
end
"""

lua_script_sha = settings.REDIS.script_load(lua_script)


@transaction.atomic
def order_create(*, user: User, coin: Coin, amount: Decimal):
    order = Order.objects.create(user=user, coin=coin, amount=amount)
    total_price = coin.price * amount
    wallet_discharge(wallet=user.wallet, amount=total_price)
    coin_list = order_list.format(coin=coin.name)
    if total_price < settings.MINIMUM_ORDER_AMOUNT:
        to_pay = settings.REDIS.evalsha(lua_script_sha, 1, coin_list, float(total_price), settings.MINIMUM_ORDER_AMOUNT)
    else:
        to_pay = total_price

    if not to_pay:
        return order

    buy_from_exchange(coin=coin, amount=to_pay)

    return order


def order_check_possibility(*, user: User, coin: Coin, amount: Decimal):
    total_price = coin.price * amount
    is_eligible = wallet_check_balance_to_buy(wallet=user.wallet, amount=total_price)
    return is_eligible
