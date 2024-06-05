from django.db import models

# Create your models here.


class Url(models.Model):
    key = models.CharField(max_length=6)
    long_url = models.URLField()
    short_url = models.URLField()

    def __str__(self):
        return self.short_url
