from rest_framework import serializers

from wallet.models import Wallet, Transaction
from wallet.services.commands import wallet_charge


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["balance"]
        read_only_fields = fields


class ChargeSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0, write_only=True)

    def create(self, validated_data):
        wallet_charge(wallet=validated_data["user"].wallet, amount=validated_data["amount"])

        return {}


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "value"]
        read_only_fields = fields
