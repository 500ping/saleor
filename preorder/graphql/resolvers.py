from ..models import PreOrder


def resolve_pre_orders():
    qs = PreOrder.objects.all()
    return qs
