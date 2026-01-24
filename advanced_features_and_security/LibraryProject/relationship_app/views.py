from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render


from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Library
from .models import Book

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book


@permission_required("relationship_app.can_view", raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})


@permission_required("relationship_app.can_create", raise_exception=True)
def create_book(request):
    return render(request, "create_book.html")


@permission_required("relationship_app.can_edit", raise_exception=True)
def edit_book(request, book_id):
    return render(request, "edit_book.html")


@permission_required("relationship_app.can_delete", raise_exception=True)
def delete_book(request, book_id):
    return render(request, "delete_book.html")

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})



def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    return HttpResponse("Add book view")


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    return HttpResponse("Edit book view")


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    return HttpResponse("Delete book view")
