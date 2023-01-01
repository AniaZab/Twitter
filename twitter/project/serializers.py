from django.contrib.auth.models import User
from rest_framework import serializers

from project.models import Post, RegisterUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ['username', 'email', 'password', 'password_confirm']


class CreateUpdatePostSerializer(serializers.HyperlinkedModelSerializer):
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
        fields = '__all__'
