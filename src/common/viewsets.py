from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ListModelViewSet(mixins.ListModelMixin, GenericViewSet):
    pass


class RetrieveModelViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    pass


class RetrieveListModelViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    pass
