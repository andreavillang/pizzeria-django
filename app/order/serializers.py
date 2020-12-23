from rest_framework import serializers
from core.models import Order, Payment

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for order objects
    """

    class Meta:
        model = Order
        fields = (
            'id',
            'date',
            'pizza',
            'quantity',
            'is_paid',
        )
        read_only_fields = ('id',)

class PaymentSerializer(serializers.ModelSerializer):
    """
    Serializer for payment objects
    """

    class Meta:
        model = Payment
        fields = (
            'id',
            'payment_method',
            'amount',
        )
        read_only_fields = ('id',)