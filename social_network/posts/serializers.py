from rest_framework import serializers
from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']
        

class PostSerializer(serializers.ModelSerializer):
    
    comments = CommentSerializer(many=True, read_only = True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'image', 'created_at', 'total_likes', 'comments']
        read_only_fields = ['author']

    def create(self, validated_data):
        comments_data = validated_data.pop('comments')
        post = Post.objects.create(**validated_data)
        for comment_data in comments_data:
            Comment.objects.create(post=post, **comment_data)
        return post

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['comments'] = list([CommentSerializer(comment).data for comment in Comment.objects.filter(post=instance)])

        return representation

