from django.urls import path, include

urlpatterns = [
    path("v1/auth/", include("apis.auth")),
    path("v1/coins/", include("coin.urls")),
    path("v1/wallet/", include("wallet.urls")),
    path("v1/orders/", include("order.urls")),
]
