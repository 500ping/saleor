from saleor.graphql.core.connection import CountableDjangoObjectType
from ..models import PreOrder
import graphene


class PreOrder(CountableDjangoObjectType):
    id = graphene.GlobalID(required=True)

    class Meta:
        model = PreOrder
