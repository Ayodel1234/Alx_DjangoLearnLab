from django.urls import path
from .views import TagPostListView, SearchResultsView
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='posts'),

    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('tags/<str:tag_name>/', TagPostListView.as_view(), name='tag-posts'),
    path('search/', SearchResultsView.as_view(), name='search-results'),

]
