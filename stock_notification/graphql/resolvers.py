from .. import models


def resolve_transfer_request(id):
    return models.TransferRequest.objects.filter(id=id).first()


def resolve_transfer_requests():
    return models.TransferRequest.objects.all()
