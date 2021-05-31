from django.contrib.postgres.fields import ArrayField
from django.db import models
from users_api.models import User
from posts_api.models import Post

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(
        "users_api.User",
        on_delete=models.SET_NULL,
        null=True,
        related_query_name="comments"
    )
    text = models.CharField(
        max_length=256,
        blank=False,
        null=True
    )
    post = models.ForeignKey(
        "posts_api.Post",
        on_delete=models.SET_NULL,
        null=True,
        related_query_name="comments"
    )
