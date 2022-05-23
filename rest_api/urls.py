from rest_api.views import OrderViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('api/v1/orders', OrderViewSet)
urlpatterns = router.urls
