from django.db import models
from saleor.order.models import Order
from saleor.core.models import ModelWithMetadata


class PreOrder(ModelWithMetadata):
    order = models.OneToOneField(
        Order,
        on_delete=models.SET_NULL,
        related_name="pre_order",
        null=True
    )
    requested_shipment_date = models.DateField()

    class Meta(ModelWithMetadata.Meta):
        ordering = ("requested_shipment_date",)
