from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination

from .permissions import AuthorOrReadOnly
from posts.models import User, Post, Group, Follow
from .serializers import (UserSerializer, PostSerializer,
                          GroupSerializer, CommentSerializer,
                          FollowSerializer)
from .pagination import PostPagination


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = PostPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs['post_id']
        )

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        return post.comments


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        author = get_object_or_404(User, username=serializer.initial_data['following'])
        serializer.save(
            user=self.request.user,
            following=author
        )
    
    def get_queryset(self):
        user = Follow.objects.filter(user=self.request.user)
        return user
