from django.urls import path

from wallet.apis import WalletViewSet

urlpatterns = [
    path("", WalletViewSet.as_view({"get": "retrieve"}), name="wallet"),
    path("transactions/", WalletViewSet.as_view({"get": "list"}), name="wallet-list"),
    path("transactions/<int:id>/", WalletViewSet.as_view({"get": "retrieve"}), name="wallet-retrieve"),
]
