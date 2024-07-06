from common.pagination import StandardResultsSetPagination
from common.viewsets import CreateRetrieveListModelViewSet
from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(CreateRetrieveListModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
