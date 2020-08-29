from rest_framework import routers
from polls.views import PollingViewSet, PizzaViewSet

router = routers.DefaultRouter()
router.register(r'polls', PollingViewSet, basename="polls")
router.register(r'pizzas', PizzaViewSet, basename="pizzas")

