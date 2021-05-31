from django.contrib.postgres.fields import ArrayField
from django.db import models
from users_api.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        "users_api.User",
        on_delete=models.SET_NULL,
        null=True,
        related_query_name="posts"
    )
    image = models.CharField(
        max_length=256,
        blank=True,
        null=True
    )
    text = models.CharField(
        max_length=256,
        blank=False,
        null=True
    )
    liked_by = ArrayField(
        models.IntegerField(),
        blank=True,
        default=list
    )
