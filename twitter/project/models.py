from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"

class Post(models.Model):
    content = models.CharField(max_length=280),
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.content

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    likedPosts = models.ManyToManyField(Post, related_name="liked_by", symmetrical=False, blank=True)
    def __str__(self):
        return self.user.__str__() + " " + self.likedPosts.__str__()