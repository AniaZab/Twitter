from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets

from project.serializers import UserSerializer
from project.serializers import PostSerializer

from project.models import Post



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
