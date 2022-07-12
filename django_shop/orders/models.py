from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    STATUS_TEXT = {
        10: 'Waiting',
        20: 'In progress',
        30: 'Sent',
        40: 'Done',
        50: 'Cancelled'
    }

    STATUS_WAITING = 10
    STATUS_IN_PROGRESS = 20
    STATUS_SENT = 30
    STATUS_DONE = 40
    STATUS_CANCELLED = 50

    price_net = models.DecimalField(null=False, max_digits=13, decimal_places=2)
    price_gross = models.DecimalField(null=False, max_digits=13, decimal_places=2)
    amount = models.IntegerField(null=False, default=1)
    # product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.PROTECT)
    # payment = models.ForeignKey(Payment, null=False, blank=False, on_delete=models.PROTECT)
    status = models.IntegerField(null=False, default=STATUS_WAITING)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)
    active = models.BooleanField(null=False, blank=False, default=True)
