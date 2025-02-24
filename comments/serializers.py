from rest_framework import serializers
from .models import Comment
from authors.serializers import AuthorSerializer



class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'parent_comment', 'replies']

    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return []

    def validate_parent_comment(self, value):
        if value and value.parent_comment and value.parent_comment.parent_comment:
            raise serializers.ValidationError("Maksimal 3 daraja izoh ruxsat berilgan.")
        return value