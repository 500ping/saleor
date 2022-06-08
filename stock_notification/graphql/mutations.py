import graphene
from saleor.graphql.core.mutations import ModelMutation, ModelDeleteMutation, \
    BaseMutation
from ..models import TransferRequest
from .types import TransferRequest as TransferRequestType
from graphene_django import DjangoObjectType


class TransferRequestInput(graphene.InputObjectType):
    source_warehouse = graphene.String(description="Source warehouse")
    dest_warehouse = graphene.String(description="Dest warehouse")
    quantity = graphene.Int(description="Quantity")
    product_id = graphene.String(description="Product")


class TransferRequestCreate(ModelMutation):
    class Arguments:
        input = TransferRequestInput(required=True,
                                     description="Fields required to create tranfer "
                                                 "request.")

    class Meta:
        description = "Creates new tranfer request."
        model = TransferRequest
        # error_type_class = CustomError
        # error_type_field = "custom_errors"

    custom = graphene.Field(TransferRequestType, description="Transfer request return")

    @classmethod
    def get_type_for_model(cls):
        return TransferRequestType

    @classmethod
    def perform_mutation(cls, _root, info, **data):
        instance = TransferRequest(
            source_warehouse=data.get('input').name,
            dest_warehouse=data.get('input').attribute,
            quantity=data.get('input').description,
            product_id=data.get('input').pick_date,
            created_by=data.get('input').new_feature,
        )
        instance.save()
        return cls.success_response(instance)
