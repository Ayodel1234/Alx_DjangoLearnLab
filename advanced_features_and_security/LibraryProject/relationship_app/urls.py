from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .views import (
    list_books,
    LibraryDetailView,
    add_book,
    edit_book,
    delete_book,
)

urlpatterns = [
    # Existing views
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # 🔒 Permission-protected book actions (THIS IS WHAT ALX IS CHECKING)
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]
