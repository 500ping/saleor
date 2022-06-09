from saleor.graphql.core.types.common import Error
from .enums import TransferRequestErrorCode


class TransferRequestError(Error, Exception):
    code = TransferRequestErrorCode(description="Transfer request error code.",
                                    required=True)
