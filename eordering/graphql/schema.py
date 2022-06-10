import graphene

from saleor.graphql.core.fields import PrefetchingConnectionField
from saleor.graphql.core.utils import from_global_id_or_error
from .mutations.orders import ChangeOrderLineProduct
from .types import EOrderType


class EOrderQueries(graphene.ObjectType):
    eorder = graphene.Field(
        EOrderType,
        description="Look up a order by ID.",
        id=graphene.Argument(
            graphene.ID, description="ID of an order", required=True
        ),
    )

    eorder = PrefetchingConnectionField(EOrderType, description="List of customs.",)

    def resolve_custom(self, info, **kwargs):
        custom_pk = kwargs.get("id")
        _, id = from_global_id_or_error(custom_pk, EOrderType)
        return resolve_eorder(id)

    def resolve_customs(self,  info, **_kwargs):
        return resolve_eorder()


class EOrderMutations(graphene.ObjectType):
    change_order_line_product = ChangeOrderLineProduct.Field()
