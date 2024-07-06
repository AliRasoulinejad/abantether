from django.urls import path, include

urlpatterns = [
    path("v1/auth/", include("apis.auth")),
    path("v1/coin/", include("coin.urls")),
    path("v1/wallet/", include("wallet.urls")),
]
