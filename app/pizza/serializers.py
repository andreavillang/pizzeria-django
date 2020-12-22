from rest_framework import serializers
from core.models import Pizza

class PizzaSerializer(serializers.ModelSerializer):
    """
    Serializer for pizza objects
    """

    class Meta:
        model = Pizza
        fields = (
            'id', 
            'name', 
            'price',
        )
        read_only_fields = ('id',)