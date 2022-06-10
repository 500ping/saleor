from django.db import models
from saleor.order.models import OrderLine
from saleor.product.models import ProductVariant


class EOrderLine(models.Model):
    core_order_line = models.OneToOneField(
        OrderLine,
        on_delete=models.Case,
        related_name="eorderline"
    )
    original_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        related_name="original_product_variant",
        null=True,
        blank=True
    )
    original_product_sku = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )


class EProductVariant(models.Model):
    original_sku = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )
