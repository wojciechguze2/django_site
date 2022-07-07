from django.db import models


class Order(models.Model):
    STATUS_TEXT = {
        10: 'Waiting',
        20: 'In progress',
        30: 'Sent',
        40: 'Done',
        50: 'Canceled'
    }
