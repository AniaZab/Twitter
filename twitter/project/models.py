from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    content = models.CharField(max_length=280),
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.content
