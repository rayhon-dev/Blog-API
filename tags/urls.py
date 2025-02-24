from django.urls import path
from .views import TagListCreateView,TagPostsView

urlpatterns = [
    path('api/tags/', TagListCreateView.as_view()),
    path('api/tags/<int:tag_id>/posts/', TagPostsView.as_view()),
]
