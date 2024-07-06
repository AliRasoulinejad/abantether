from rest_framework.routers import SimpleRouter

from coin.apis import CoinViewSet

router = SimpleRouter()
router.register("", CoinViewSet)

urlpatterns = router.urls
