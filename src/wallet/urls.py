from django.urls import path

from wallet.apis import WalletViewSet, TransactionViewSet

urlpatterns = [
    path("", WalletViewSet.as_view({"get": "retrieve"}), name="wallet"),
    path("charge/", WalletViewSet.as_view({"post": "charge"}), name="wallet-charge"),
    path("transactions/", TransactionViewSet.as_view({"get": "list"}), name="wallet-list"),
    path("transactions/<int:pk>/", TransactionViewSet.as_view({"get": "retrieve"}), name="wallet-retrieve"),
]
