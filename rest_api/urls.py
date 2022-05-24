from rest_api.views import OrderViewSet, OrderChartViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('v1/orders/chart', OrderChartViewSet)
router.register('v1/orders', OrderViewSet)
urlpatterns = router.urls
