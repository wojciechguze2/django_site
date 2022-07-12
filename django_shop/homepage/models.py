from django.db import models


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False, blank=False)
    short_description = models.CharField(max_length=2048, null=True, blank=False)
    description = models.CharField(max_length=16384, null=False, blank=False)
    image_url = models.URLField(null=True, blank=True)
    active = models.BooleanField(null=False, blank=False, default=True)
    create_date = models.DateTimeField(null=False, auto_now_add=True)
    last_modification = models.DateTimeField(null=False, auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['id']

    def to_repr(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'short_description': self.short_description,
            'image_url': self.image_url
        }
