from django.db import models
from saleor.core.models import ModelWithMetadata
from saleor.warehouse.models import Warehouse
from saleor.product.models import ProductVariant
from saleor.account.models import User


class TransferRequest(ModelWithMetadata):
    source_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE,
                                         related_name='source_warehouse')
    dest_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE,
                                       related_name='dest_warehouse')
    quantity = models.IntegerField()
    product = models.ForeignKey(ProductVariant, on_delete=models.CASCADE,
                                related_name='+')

    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='created_by')
    created_on = models.DateTimeField(auto_now_add=True)

    approved_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='approved_by', null=True,
                                    blank=True)
    approved_on = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
