from datetime import datetime

import graphene
from saleor.graphql.core.mutations import ModelMutation, BaseMutation
from saleor.core.permissions import AccountPermissions
from .TransferRequestError import TransferRequestError, TransferRequestErrorCode
from .types import TransferRequest as TransferRequestType
from .. import models
from .utils import check_stock_quantity, create_or_update_stock, update_source_stock_quantity


class TransferRequestCreateInput(graphene.InputObjectType):
    source_warehouse = graphene.ID(description='Source warehouse global id.',
                                   required=True)
    dest_warehouse = graphene.ID(description='Source destination global id.',
                                 required=True)
    quantity = graphene.Int(description='Product quantity', required=True)
    product = graphene.ID(description='Product global id.', required=True)


class TransferRequestCreate(ModelMutation):
    class Arguments:
        input = TransferRequestCreateInput(
            required=True, description="Fields required to create a transfer request."
        )

    class Meta:
        description = "Creates a new transfer request."
        model = models.TransferRequest
        permissions = (AccountPermissions.MANAGE_USERS,)
        error_type_class = TransferRequestError
        error_type_field = "transfer_request_errors"

    transfer_request = graphene.Field(TransferRequestType,
                                      description="transfer request type return")

    @classmethod
    def get_instance(cls, info, **data):
        instance = super().get_instance(info, **data)
        user = info.context.user
        if user.is_authenticated:
            instance.created_by = user
        return instance

    @classmethod
    def clean_input(cls, info, instance, data):
        cleaned_input = super().clean_input(info, instance, data)

        quantity = cleaned_input.get("quantity")
        source = cleaned_input.get("source_warehouse")
        product = cleaned_input.get("product")

        check_stock_quantity(source, quantity, product)

        return cleaned_input

    @classmethod
    def perform_mutation(cls, _root, info, **data):
        res = super().perform_mutation(_root, info, **data)
        return res


class ApproveTransferInput(graphene.InputObjectType):
    message = graphene.String(description="Reason...")


class ApproveTransferRequest(ModelMutation):
    class Arguments:
        id = graphene.ID(description="ID of transfer request.", required=True)
        input = ApproveTransferInput("Fields for approve transfer request.")

    class Meta:
        description = "Approve a transfer request."
        model = models.TransferRequest
        permissions = (AccountPermissions.MANAGE_STAFF,)
        error_type_class = TransferRequestError
        error_type_field = "transfer_request_errors"

    transfer_request = graphene.Field(TransferRequestType,
                                      description="transfer request type return")

    @classmethod
    def get_instance(cls, info, **data):
        instance = super().get_instance(info, **data)
        update_source_stock_quantity(instance.source_warehouse, instance.quantity, instance.product)
        create_or_update_stock(instance.dest_warehouse, instance.quantity, instance.product)

        user = info.context.user
        if user.is_authenticated:
            instance.approved_by = user
            instance.approved_on = datetime.now()
            instance.status = True

        print(instance)

        return instance

    # @classmethod
    # def perform_mutation(cls, root, info, **data):
    #     transfer_request = cls.get_node_or_error(info, data.get('id'), TransferRequestType)
