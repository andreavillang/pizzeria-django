from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pizza import views

# DefaultRouter is from DjangoRest that generates the urls for our view
router = DefaultRouter()
router.register('pizzas', views.PizzaViewSet)
#router.register('ingredients', views.IngredientViewSet)

app_name = 'pizza'

urlpatterns = [
    path('', include(router.urls))
]