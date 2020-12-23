from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order import views

# DefaultRouter is from DjangoRest that generates the urls for our view
router = DefaultRouter()
router.register('orders', views.OrderViewSet)
#router.register('payments', views.PaymentViewSet)

app_name = 'order'

urlpatterns = [
    path('', include(router.urls))
]