import graphene
from ..models import TransferRequest
from saleor.graphql.core.connection import CountableDjangoObjectType


# class TransferRequest(CountableDjangoObjectType):
#     id = graphene.GlobalID(required=True)
#
#     class Meta:
#         model = TransferRequest
