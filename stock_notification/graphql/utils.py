from saleor.warehouse.models import Stock
from .TransferRequestError import TransferRequestError
from ..error_codes import TransferRequestErrorCode
from django.core.exceptions import ValidationError


def check_stock_quantity(source, quantity_requested, product_variant):
    stock = Stock.objects.filter(warehouse=source,
                                 product_variant=product_variant).first()
    if not stock:
        raise TransferRequestError(
            TransferRequestErrorCode.PRODUCT_NOT_IN_WAREHOUSE.value,
            code=TransferRequestErrorCode.PRODUCT_NOT_IN_WAREHOUSE)
    if stock.quantity < quantity_requested:
        raise TransferRequestError(
            TransferRequestErrorCode.STOCK_NOT_VALID.value,
            code=TransferRequestErrorCode.STOCK_NOT_VALID)


def update_source_stock_quantity(source, quantity, product_variant):
    stock = Stock.objects.filter(warehouse=source,
                                 product_variant=product_variant).first()

    if stock:
        stock.quantity -= quantity
        stock.save()

    return


def create_or_update_stock(dest, quantity, product_variant):
    stock = Stock.objects.filter(warehouse=dest,
                                 product_variant=product_variant).first()

    if not stock:
        new_stock = Stock(
            warehouse=dest,
            product_variant=product_variant,
            quantity=quantity
        )
        new_stock.save()
    else:
        stock.quantity += quantity
        stock.save()

    return
