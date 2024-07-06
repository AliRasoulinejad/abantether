from rest_framework import serializers

from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ["id", "user", "coin"]
        read_only_fields = fields
