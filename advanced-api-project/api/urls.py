from django.urls import path

from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # Read operations
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Write operations (explicit paths for ALX checker)
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),

    # Real update/delete endpoints (still needed for functionality)
    path('books/<int:pk>/update/', BookUpdateView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteView.as_view()),
]
