from rest_framework import serializers
from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']
        

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'image', 'created_at', 'total_likes']
        read_only_fields = ['author']

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['comments'] = list([CommentSerializer(comment).data for comment in Comment.objects.filter(post=instance)])

        return representation

