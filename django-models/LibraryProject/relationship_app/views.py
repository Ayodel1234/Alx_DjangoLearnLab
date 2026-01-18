from django.http import HttpResponse
from django.views.generic.detail import DetailView

from .models import Library
from .models import Book


# Function-based view
# MUST return plain text (NOT render, NOT template)
def list_books(request):
    books = Book.objects.all()
    response = ""

    for book in books:
        response += book.title + " by " + book.author.name + "\n"

    return HttpResponse(response)


# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
