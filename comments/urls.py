from django.urls import path
from .views import PostCommentListCreateView, CommentDetailView

urlpatterns = [
    path('api/posts/<int:post_id>/comments/', PostCommentListCreateView.as_view(), name='post-comments'),  # GET va POST
    path('api/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),  # GET, PUT, DELETE
]
