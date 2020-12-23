from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from core.models import Order, Payment

from order import serializers

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    """
    Manage orders in the database
    """

    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # payment_serializer = serializers.PaymentSerializer
    # queryset_payment = Payment.objects.all()

    def get_queryset(self):
        """
        Retrieve the order for the authenticated user
        """

        #return self.queryset.filter(user=self.request.user).order_by('-date')
        return self.queryset.order_by('-date')

    # def get_payment_details(self):
    #     """
    #     Retrieve payment details
    #     """
    #     return self.queryset_payment
    
    def perform_create(self, serializer):
        """
        Create a new order
        """
        # By default, Django already knows how to make the Recipe object. This line of code ties it to the user.
        # serializer.save(user=self.request.user)
        serializer.save()