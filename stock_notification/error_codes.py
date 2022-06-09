from enum import Enum


class TransferRequestErrorCode(str, Enum):
    STOCK_NOT_VALID = 'Stock not valid!!!!'
    PRODUCT_NOT_IN_WAREHOUSE = 'Product is not available in source warehouse!!!!'
