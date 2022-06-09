import graphene

from saleor.graphql.channel import ChannelContext
from .. import models
from saleor.warehouse.models import Warehouse
from saleor.graphql.core.connection import CountableDjangoObjectType


class TransferRequest(CountableDjangoObjectType):
    id = graphene.GlobalID(required=True)

    class Meta:
        model = models.TransferRequest

    @staticmethod
    def resolve_product(root, *_args):
        return ChannelContext(node=root.product, channel_slug=None)
