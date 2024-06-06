from django.db import models

# Create your models here.


class Url(models.Model):
    key = models.CharField(max_length=6)
    long_url = models.URLField()
    short_url = models.URLField()

    # def __str__(self):
    #     return f"key:{self.key}, long_url:{self.long_url}, short_url:{self.short_url}"
