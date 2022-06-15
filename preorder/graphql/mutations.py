import graphene

from saleor.core.permissions import OrderPermissions
from saleor.core.tracing import traced_atomic_transaction
from saleor.graphql.core.mutations import ModelMutation
from saleor.graphql.core.types.common import OrderError
from saleor.order.models import Order

from ..models import PreOrder


class PreOrderCreateInput(graphene.InputObjectType):
    requested_shipment_date = graphene.Date(
        description="The date that customer want the product to be shipped"
    )


class PreOrderCreate(ModelMutation):
    requested_shipment_date = graphene.String(
        description="The date that customer want the product to be shipped"
    )

    class Arguments:
        id = graphene.ID(required=True, description="ID of an order to update.")
        input = PreOrderCreateInput(
            required=True, description="Fields required to create an pre order."
        )

    class Meta:
        description = "update requested shipment date for order."
        model = Order
        permissions = (OrderPermissions.MANAGE_ORDERS,)
        error_type_class = OrderError
        error_type_field = "order_errors"

    @staticmethod
    def _set_preorder_date(info, instance, cleaned_input):
        PreOrder.objects.create(
            order=instance,
            requested_shipment_date=cleaned_input.get("requested_shipment_date")
        )

    @classmethod
    def perform_mutation(cls, _root, info, **data):
        instance = cls.get_instance(info, **data)
        data = data.get("input")
        cleaned_input = cls.clean_input(info, instance, data)
        cls._set_preorder_date(info, instance, cleaned_input)
        return cls.success_response(instance)

    @classmethod
    def success_response(cls, instance):
        """Return a success response."""
        response = super().success_response(instance)
        response.requested_shipment_date = instance.pre_order.requested_shipment_date
        return response
