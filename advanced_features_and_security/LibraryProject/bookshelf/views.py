from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Resource

from django.contrib.auth.decorators import login_required
from .forms import ResourceForm




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



@login_required
def book_list(request):
    books = Resource.objects.all()  # ORM = safe from SQL injection
    return render(request, "bookshelf/book_list.html", {"books": books})


@login_required
def create_book(request):
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ResourceForm()

    return render(request, "bookshelf/form_example.html", {"form": form})