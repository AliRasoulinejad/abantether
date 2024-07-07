from config.env import env

MINIMUM_ORDER_AMOUNT = env.int("MINIMUM_ORDER_AMOUNT", default=0)
