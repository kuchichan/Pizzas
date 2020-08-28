from rest_framework import routers
from polls.views import PollingViewSet, PizzaViewSet

router = routers.DefaultRouter()
router.register(r'polls', PollingViewSet)
router.register(r'pizzas', PizzaViewSet)

