import graphene
from saleor.graphql.core.mutations import ModelMutation
from saleor.graphql.core.types.common import OrderError
from saleor.core.permissions import OrderPermissions

from ... import models
from ...events import change_order_line_product


class ChangeOrderLineProductInput(graphene.InputObjectType):
    product_variant_id = graphene.ID(
        description='Product Variant ID.',
        required=True
    )


class ChangeOrderLineProduct(ModelMutation):
    class Arguments:
        id = graphene.ID(description="ID of a custom update.", required=True)
        input = ChangeOrderLineProductInput(
            required=True,
            description="Fields required to change order line product."
        )

    class Meta:
        description = "Change order line product."
        model = models.OrderLine
        # permissions = (OrderPermissions.MANAGE_ORDERS,)
        error_type_class = OrderError
        error_type_field = "order_errors"

    @classmethod
    def get_instance(cls, info, **data):
        instance = super().get_instance(info, **data)
        data = data.get('input')
        new_variant = cls.get_node_or_error(info, data.product_variant_id)
        instance = change_order_line_product(instance, new_variant)
        return instance
