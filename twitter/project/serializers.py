from django.contrib.auth.models import User
from rest_framework import serializers

from project.models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class CreatePostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

class EmptySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = []

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        #user
        #likedBy
        fields = '__all__' #['title', 'content']
