from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class Post(models.Model):
    title = models.CharField(max_length=100, default='', null=True)
    content = models.CharField(max_length=280, default='', null=True)
    user = models.ForeignKey(User, related_name="created_by", on_delete=models.PROTECT)
    likedBy = models.ManyToManyField(User, related_name="liked_by", symmetrical=False, blank=True)

    def __str__(self):
        return self.title + " " + self.content
