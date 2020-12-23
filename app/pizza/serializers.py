from rest_framework import serializers
from core.models import Pizza, Ingredient

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
            'ingredients',
        )
        read_only_fields = ('id',)

class IngredientSerializer(serializers.ModelSerializer):
    """
		Serializer for ingredient objects
		"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)

class PizzaDetailSerializer(PizzaSerializer):
    """
    Serialize a pizza detail
    """

    ingredients = IngredientSerializer(many=True, read_only=True)