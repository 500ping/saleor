import graphene
from .. import error_codes

TransferRequestErrorCode = graphene.Enum.from_enum(error_codes.TransferRequestErrorCode)
