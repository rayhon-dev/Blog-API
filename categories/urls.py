from django.urls import path
from .views import CategoryListCreateView, CategoryPostsView

urlpatterns = [
    path('api/categories/', CategoryListCreateView.as_view()),
    path('api/categories/<int:category_id>/posts/', CategoryPostsView.as_view()),
]
