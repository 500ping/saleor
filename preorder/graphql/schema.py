import graphene
from .mutations import PreOrderCreate
from .types import PreOrder
from saleor.graphql.core.fields import PrefetchingConnectionField
from .resolvers import resolve_pre_orders


class PreOrderQueries(graphene.ObjectType):
    pre_orders = PrefetchingConnectionField(PreOrder, description="List of customs.")

    def resolve_pre_orders(self, info, **_kwargs):
        return resolve_pre_orders()


class PreOrderMutations(graphene.ObjectType):
    create_pre_order = PreOrderCreate.Field()
