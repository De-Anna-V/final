from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet
from posts.permissions import Permitted

from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, Permitted]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    




@api_view(['GET'])
def posts_list_view(request):
    posts = Post.objects.all()
    serialised_posts = PostSerializer(posts, many = True)
    return Response(serialised_posts.data)

@api_view(['GET'])
def comments_list_view(request):
    comments = Comment.objects.all()
    serialised_comments = CommentSerializer(comments, many = True)
    return Response(serialised_comments.data)
