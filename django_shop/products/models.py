from django.db import models

from django_shop.settings import DEFAULT_CURRENCY, DEFAULT_LENGTH_UNIT, DEFAULT_WEIGHT_UNIT


def default_image_urls():
    return []


def default_recommendations():
    return [{
        'product_id': 0,
        'thumb_urls': ''
    }]


class Product(models.Model):
    short_fields = ['id',
                    'name',
                    'short_description',
                    'thumb_url',
                    'price_gross',
                    'front_price_gross',
                    'currency']

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512, null=False, blank=False)
    short_description = models.CharField(max_length=1024, null=True, blank=True)
    description = models.CharField(max_length=8192, null=True, blank=True)
    price_net = models.DecimalField(null=False, max_digits=13, decimal_places=2)
    vat_percent = models.IntegerField(null=False, blank=False, default=23)
    currency = models.CharField(max_length=6, null=False, blank=False, default=DEFAULT_CURRENCY)
    discount_percent = models.IntegerField(null=False, blank=False, default=0)
    active = models.BooleanField(null=False, blank=False, default=False)
    available_amount = models.IntegerField(null=False, default=0)
    weight = models.DecimalField(null=True, blank=True, max_digits=13, decimal_places=4)
    weight_unit = models.CharField(max_length=6, null=False, default=DEFAULT_WEIGHT_UNIT)
    width = models.CharField(max_length=16, null=True)
    height = models.CharField(max_length=16, null=True)
    length = models.CharField(max_length=16, null=True)
    length_unit = models.CharField(max_length=6, null=False, default=DEFAULT_LENGTH_UNIT)
    thumb_url = models.URLField(null=True, blank=True)
    image_urls = models.JSONField(null=True, default=default_image_urls)
    recommendations = models.JSONField(null=True, default=default_recommendations)
    create_date = models.DateTimeField(null=False, auto_now_add=True)
    last_modification = models.DateTimeField(null=False, auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']

    @property
    def front_price_gross(self):
        return round(float(self.price_gross) - float(self.price_gross) * (self.discount_percent / 100), 2)

    @property
    def price_gross(self):
        return round(float(self.price_net) + float(self.price_net) * (self.vat_percent / 100), 2)

    def to_repr(self):
        return {
            'id': self.id,
            'name': self.name,
            'short_description': self.short_description,
            'price_gross': self.price_gross,
            'front_price_gross': self.front_price_gross,
            'currency': self.currency,
            'thumb_url': self.thumb_url
        }

