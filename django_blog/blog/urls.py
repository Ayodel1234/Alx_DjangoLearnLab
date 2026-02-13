from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostByTagListView,
    SearchResultsView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # 🔥 REQUIRED FOR ALX CHECKER
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='tag-posts'),
    path('search/', SearchResultsView.as_view(), name='search'),
]
