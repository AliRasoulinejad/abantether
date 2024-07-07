from rest_framework import status
from rest_framework.response import Response

from common.pagination import StandardResultsSetPagination
from common.viewsets import RetrieveListModelViewSet, RetrieveModelViewSet
from wallet.models import Wallet, Transaction
from wallet.serializers import TransactionSerializer, WalletSerializer, ChargeSerializer


class WalletViewSet(RetrieveModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def get_object(self):
        return self.request.user.wallet

    def charge(self, request, *args, **kwargs):
        self.serializer_class = ChargeSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class TransactionViewSet(RetrieveListModelViewSet):
    serializer_class = TransactionSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Transaction.objects.filter(wallet=self.request.user.wallet)
