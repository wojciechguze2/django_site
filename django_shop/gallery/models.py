from django.db import models


class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    image_url = models.URLField(null=False, blank=False)
    active = models.BooleanField(null=False, blank=False, default=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']

    def to_repr(self):
        return {
            'id': self.id,
            'image_url': self.image_url
        }