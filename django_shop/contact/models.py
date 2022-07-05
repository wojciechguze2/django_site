from django.db import models


class ContactModel(models.Model):
    identity = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    description = models.CharField(max_length=2048, blank=True, null=True)

    objects = models.Manager()
