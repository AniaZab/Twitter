from django.contrib.auth.models import User
from rest_framework import serializers

from project.models import Post, Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['content']
class ProfileSerializer(serializers.HyperlinkedModelSerializer): #ModelSerializer
    class Meta:
        model = Profile
        fields = '__all__'