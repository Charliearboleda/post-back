from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    posts = ArrayField(models.IntegerField())
    following = ArrayField(models.IntegerField())
    followers = ArrayField(models.IntegerField())
