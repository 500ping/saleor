from saleor.order.models import Order


def resolve_custom(pk):
    return Order.objects.filter(pk=pk).first()


def resolve_stocks():
    return Order.objects.all()
