from rest_framework import serializers

from order.models import Order
from order.services.commands import order_create


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ["id", "user", "coin", "amount"]
        read_only_fields = fields

    def create(self, validated_data):
        order = order_create(user=validated_data["user"], coin=validated_data["coin"], amount=validated_data["amount"])

        return order
