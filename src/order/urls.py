from rest_framework.routers import SimpleRouter

from order.apis import OrderViewSet

router = SimpleRouter()
router.register("", OrderViewSet)

urlpatterns = router.urls
