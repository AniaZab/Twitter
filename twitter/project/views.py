from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import re_path
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.core import serializers

from project.serializers import UserSerializer, PostSerializer, CreatePostSerializer, EmptySerializer

from project.models import Post, User
from rest_framework.response import Response
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.GenericViewSet):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['GET'], url_path='get-post-list', permission_classes=[IsAuthenticated, ])
    def get_post_list(self, request):
        return Response(serializers.serialize('json', self.queryset))
    @action(detail=False, methods=['GET'], url_path='get-post-list-created-by-logged-user', permission_classes=[IsAuthenticated, ])
    def get_post_list_created_by_logged_user(self, request):
        return Response(serializers.serialize('json', self.model.objects.filter(user=request.user)))
    @action(detail=False, methods=['GET'], url_path='get-post-list-liked-by-logged-user', permission_classes=[IsAuthenticated, ])
    def get_post_list_liked_by_logged_user(self, request):
        return Response(serializers.serialize('json', self.model.objects.filter(likedBy=request.user)))

    @action(detail=True, methods=['GET'], url_path='get-post-list-created-by',
            permission_classes=[IsAuthenticated, ])
    def get_post_list_created_by_user(self, request, pk=None):
        return Response(serializers.serialize('json', self.model.objects.filter(user=pk)))

    @action(detail=True, methods=['GET'], url_path='get-post-list-liked-by',
            permission_classes=[IsAuthenticated, ])
    def get_post_list_liked_by_user(self, request, pk=None):
        return Response(serializers.serialize('json', self.model.objects.filter(likedBy=pk)))

    @swagger_auto_schema(request_body=CreatePostSerializer)
    @action(detail=True, methods=['PUT'], url_path='change-post', permission_classes=[IsAuthenticated, ])
    def change_post(self, request, pk=None):
        post = get_object_or_404(self.model, pk=pk)
        post_req = request.data
        post.title = post_req["title"]
        post.content = post_req["content"]
        post.save()
        return Response("Post changed!")

    @swagger_auto_schema(request_body=CreatePostSerializer)
    @action(detail=False, methods=['POST'], url_path='add-post', permission_classes=[IsAuthenticated, ])
    def create_new_post(self, request):
        post_data = request.data

        new_post = Post.objects.create(
            title=post_data["title"],
            content=post_data["content"],
            user=request.user
        )

        new_post.save()

        return Response("Post created!")

    @action(detail=True, methods=['GET'], url_path='get-post-details', permission_classes=[IsAuthenticated, ])
    def get_single_post(self, request, pk=None):
        return Response(serializers.serialize('json', [get_object_or_404(self.model, pk=pk), ])[1:-1])

    @swagger_auto_schema(request_body=EmptySerializer)
    @action(detail=True, methods=['PUT'], url_path='like-or-dislike-post', permission_classes=[IsAuthenticated, ])
    def like_or_dislike_post(self, request, pk=None):
        post = get_object_or_404(self.model, pk=pk)
        if post.likedBy.contains(request.user):
            post.likedBy.remove(request.user)
            post.save()
            return Response("Post disliked!")
        else:
            post.likedBy.add(request.user)
            post.save()
            return Response("Post liked!")
