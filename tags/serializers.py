from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'posts_count']

    def get_posts_count(self, obj):
        return obj.posts.count()

    def create(self, validated_data):
        validated_data['slug'] = validated_data['name'].lower().replace(' ', '-')
        return super().create(validated_data)
