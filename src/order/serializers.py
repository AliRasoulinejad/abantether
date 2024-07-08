from django.core.exceptions import ValidationError
from rest_framework import serializers

from order.models import Order
from order.services.commands import order_create, order_check_possibility


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ["id", "user", "coin", "amount"]
        read_only_fields = ["id"]

    def validate(self, attrs):
        if not order_check_possibility(user=attrs["user"], coin=attrs["coin"], amount=attrs["amount"]):
            raise ValidationError(code="required_balance", message="increase your account balance")
        return attrs

    def create(self, validated_data):
        return order_create(user=validated_data["user"], coin=validated_data["coin"], amount=validated_data["amount"])
