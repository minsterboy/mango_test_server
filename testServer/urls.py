from django.urls import path
from .views import PostListCreateView, PostDetailView, post_create

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('write/', post_create.send, name='post_create'),
]
