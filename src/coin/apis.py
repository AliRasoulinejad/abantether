from rest_framework import permissions

from coin.models import Coin
from coin.serializers import CoinSerializer
from common.pagination import StandardResultsSetPagination
from common.viewsets import ListModelViewSet


class CoinViewSet(ListModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    pagination_class = StandardResultsSetPagination
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
