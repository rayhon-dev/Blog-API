from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tag
from .serializers import TagSerializer
from posts.serializers import Post, PostSerializer



class TagListCreateView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagPostsView(APIView):
    def get(self, request, tag_id):
        posts = Post.objects.filter(tags__id=tag_id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
