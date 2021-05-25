from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.IntegerField()
    image = models.CharField(max_length=128)
    text = models.CharField(max_length=140)
    liked_by = ArrayField(models.IntegerField())
    comments = ArrayField(models.IntegerField())
