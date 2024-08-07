from rest_framework import serializers

from coin.models import Coin


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ["id", "name", "price"]
        read_only_fields = ["id", "name", "price"]
