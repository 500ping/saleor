import django_filters
from saleor.graphql.core.types import FilterInputObjectType
from graphene_django.filter import GlobalIDMultipleChoiceFilter
from .. import models


class TransferRequestFilter(django_filters.FilterSet):
    status = django_filters.BooleanFilter()

    class Meta:
        model = models.TransferRequest
        fields = ['status']


class TransferRequestFilterInput(FilterInputObjectType):
    class Meta:
        filterset_class = TransferRequestFilter
