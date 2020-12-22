from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from core.models import Pizza

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
