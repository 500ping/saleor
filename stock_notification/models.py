from datetime import datetime

from django.conf import settings
from django.db import models
from saleor.core.models import ModelWithMetadata
from saleor.warehouse.models import Warehouse
from saleor.product.models import ProductVariant
from saleor.account.models import User


class TransferRequest(ModelWithMetadata):
    # id = models.AutoField(primary_key=True)
    source_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE,
                                         related_name="source_warehouse")
    dest_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE,
                                       related_name="dest_warehouse")
    quantity = models.IntegerField()
    product_id = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,
                                   related_name="product_id")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name="created_by")
    created_on = models.DateTimeField(default=datetime.now())
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name="created_by", null=True, blank=True)
    approved_on = models.DateTimeField(null=True, blank=True)
