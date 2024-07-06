from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CreateRetrieveListModelViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet
):
    pass


class ListModelViewSet(mixins.ListModelMixin, GenericViewSet):
    pass


class RetrieveModelViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    pass


class RetrieveListModelViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    pass
