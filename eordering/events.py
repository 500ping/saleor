from django.core.exceptions import ValidationError

from .models import OrderLine
from .models import ProductVariant
from .models import EOrderLine


def change_order_line_product(order_line, new_product_variant):
    if not new_product_variant:
        raise ValidationError(
            "Invalid product variant."
        )

    # Set original order line variant and sku
    eorderline = EOrderLine(
        core_order_line=order_line,
        original_variant=order_line.variant,
        original_product_sku=order_line.product_sku
    )
    eorderline.save()

    # Update new variant to order line
    order_line.variant = new_product_variant
    order_line.product_sku = new_product_variant.sku
    order_line.save()

    return order_line

