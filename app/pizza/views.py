from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from core.models import Pizza, Ingredient

from pizza import serializers

class PizzaViewSet(viewsets.ModelViewSet):
    """
    Manage pizzas in the database
    """

    serializer_class = serializers.PizzaSerializer
    queryset = Pizza.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Retrieve the pizza for the authenticated user
        """

        return self.queryset.filter(user=self.request.user).order_by('-id')
   
    def perform_create(self, serializer):
        """
        Create a new recipe
        """
        # By default, Django already knows how to make the Recipe object. This line of code ties it to the user.
        serializer.save(user=self.request.user)

class IngredientViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    Manage ingredients in the database
    """
    # This will require the access to have a token
    authentication_classes = (TokenAuthentication,)
    # This will require the access to be from an authenticated user/token
    permission_classes = (IsAuthenticated,)

    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer

    def get_queryset(self):
        """
        Return objects based on the user.
        """
        return self.queryset.filter(user=self.request.user).order_by('-name')
    
    def get_serializer_class(self):
        """
        Return appropriate serializer class
        """

        if self.action == 'retrieve':
            return serializers.PizzaDetailSerializer
            # Remember if you dont have a return at the end of the function
            # it will crash. This ensures that If theres no specific serializer i want,
            # return the default
        return self.serializer_class
    
    def perform_create(self, serializer):
        """
        Create new Ingredient
        """

        serializer.save(user = self.request.user)
