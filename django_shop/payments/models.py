from django.db import models


class Payment(models.Model):
    STATUS_TEXT = {
        10: 'Waiting',
        20: 'In progress',
        30: 'Payed',
        40: 'Cancelled',
        50: 'Refused'
    }

    STATUS_WAITING = 10
    STATUS_IN_PROGRESS = 20
    STATUS_PAYED = 30
    STATUS_CANCELLED = 40
    STATUS_REFUSED = 50

    id = models.AutoField(primary_key=True)
    price_paid = models.DecimalField(null=False, max_digits=13, decimal_places=2)
    date_paid = models.DateTimeField(null=True)
    status = models.IntegerField(null=False, default=STATUS_WAITING)
    active = models.BooleanField(null=False, blank=False, default=True)
    create_date = models.DateTimeField(null=False, auto_now_add=True)
    last_modification = models.DateTimeField(null=False, auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']
