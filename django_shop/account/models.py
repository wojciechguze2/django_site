import uuid
from datetime import datetime, timedelta, timezone

from django.contrib.auth.models import User
from django.db import models


class PasswordChange(models.Model):
    hash = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False, null=False, blank=False)
    expires = models.DateTimeField(default=datetime.now(tz=timezone.utc) + timedelta(hours=1),
                                   blank=False, null=False)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)

    objects = models.Manager()
