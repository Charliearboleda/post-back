from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Comment(models.Model):
    author = models.IntegerField(
        blank=False,
        null=True
    )
    text = models.CharField(
        max_length=256,
        blank=False,
        null=True
    )
    post = models.IntegerField(
        blank=False,
        null=True
    )
