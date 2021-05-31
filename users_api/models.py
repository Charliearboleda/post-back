from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(
        unique=True,
        max_length=64,
        blank=False
    )
    displayName = models.CharField(
        max_length=64,
        blank=False,
        null=True
    )
    tagLine = models.CharField(
        max_length=128,
        blank=False,
        null=True
    )
    following = models.ManyToManyField(
        "User",
        blank=True
    )
