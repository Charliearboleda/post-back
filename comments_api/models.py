from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Comment(models.Model):
    author = models.IntegerField()
    text = models.CharField(max_length=256)
    post_id = models.IntegerField()
