from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.IntegerField(blank=False)
    image = models.CharField(max_length=256, blank=True, null=True)
    text = models.CharField(max_length=256, blank=False)
    liked_by = ArrayField(models.IntegerField())
    comments = ArrayField(models.IntegerField())
