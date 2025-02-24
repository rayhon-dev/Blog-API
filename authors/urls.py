from django.urls import path
from .views import AuthorListCreateView, AuthorDetailView

urlpatterns = [
    path('api/authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('api/authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]
