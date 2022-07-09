import uuid

from django.contrib.auth.models import User
from django.db import models


class PasswordChange(models.Model):
    hash = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False, null=False, blank=False)
    expires = models.DateTimeField(blank=False, null=False)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)

    objects = models.Manager()
