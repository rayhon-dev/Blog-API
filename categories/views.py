from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer
from django.http import Http404
from posts.serializers import PostSerializer, Post


class CategoryListCreateView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)



class CategoryPostsView(APIView):
    def get(self, request, category_id):
        posts = Post.objects.filter(category_id=category_id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

