from django.contrib.auth.models import User
from django.db import models

from django_shop.payments.models import Payment
from django_shop.products.models import Product
from django_shop.settings import DEFAULT_CURRENCY


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

    id = models.AutoField(primary_key=True)
    price_net = models.DecimalField(null=False, max_digits=13, decimal_places=2)
    vat_percent = models.IntegerField(null=False, blank=False, default=23)
    currency = models.CharField(max_length=6, null=False, blank=False, default=DEFAULT_CURRENCY)
    amount = models.IntegerField(null=False, default=1)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.PROTECT)
    payment = models.ForeignKey(Payment, null=True, blank=True, on_delete=models.PROTECT)
    status = models.IntegerField(null=False, default=STATUS_WAITING)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)
    active = models.BooleanField(null=False, blank=False, default=True)
    create_date = models.DateTimeField(null=False, auto_now_add=True)
    last_modification = models.DateTimeField(null=False, auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']

    def to_repr(self):
        return {
            'id': self.id,
            'product': self.product.to_short_repr(),
            'price_gross': self.price_gross,
            'amount': self.amount,
            'currency': self.currency,
            'create_date': self.create_date.strftime('%d.%m.%Y'),
            'status_text': self.STATUS_TEXT[self.status],
            'status': self.status
        }

    @property
    def price_gross(self):
        return round(float(self.price_net) + float(self.price_net) * (self.vat_percent / 100), 2)
