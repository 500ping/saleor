import graphene

from saleor.graphql.core.connection import CountableDjangoObjectType
from saleor.order.models import Order
from ..models import OrderLine
from saleor.graphql.channel import ChannelContext
from saleor.graphql.order.types import OrderLine


class EOrderType(CountableDjangoObjectType):
    id = graphene.GlobalID(required=True)

    class Meta:
        model = Order

    def resolve_variant(root, *_args):
        return ChannelContext(node=root.variant, channel_slug=None)

    def resolve_eorderline(root, *_args):
        return ChannelContext(node=root.eorderline, channel_slug=None)


# class OrderLine(OrderLine):
#
#     @staticmethod
#     def resolve_eorderline(root, *_args):
#         return ChannelContext(node=root.eorderline, channel_slug=None)
