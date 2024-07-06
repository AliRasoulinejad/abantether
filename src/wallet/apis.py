from common.pagination import StandardResultsSetPagination
from common.viewsets import RetrieveListModelViewSet, RetrieveModelViewSet
from wallet.models import Wallet, Transaction
from wallet.serializers import TransactionSerializer, WalletSerializer


class WalletViewSet(RetrieveModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def get_object(self):
        return self.request.user.wallet


class TransactionViewSet(RetrieveListModelViewSet):
    serializer_class = TransactionSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Transaction.objects.filter(wallet=self.request.user.wallet)
