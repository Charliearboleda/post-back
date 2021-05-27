from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Comment(models.Model):
    author = models.IntegerField()
    post = models.IntegerField()
    text = models.CharField(max_length=140)
