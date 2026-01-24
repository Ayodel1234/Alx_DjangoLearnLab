from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Resource


@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Resource.objects.all()
    return render(request, "books.html", {"books": books})


@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    return render(request, "create_book.html")


@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    return render(request, "edit_book.html")


@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    return render(request, "delete_book.html")