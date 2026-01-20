from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .views import list_books
from .views import LibraryDetailView

from .views import admin_view, librarian_view, member_view

from .views import add_book, edit_book, delete_book



urlpatterns = [
    # Existing views
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    path('admin/', admin_view, name='admin_view'), path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),


]
