from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints.
    """

    def setUp(self):
        """
        Set up test data for each test.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        self.author = Author.objects.create(name="Test Author")

        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

    def authenticate(self):
        """
        Authenticate test client.
        """
        self.client.login(username="testuser", password="testpassword")

    # ---------------- READ TESTS ----------------

    def test_list_books(self):
        """
        Test retrieving list of books (public access).
        """
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_single_book(self):
        """
        Test retrieving a single book by ID.
        """
        response = self.client.get(f"/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    # ---------------- CREATE ----------------

    def test_create_book_requires_authentication(self):
        """
        Ensure unauthenticated users cannot create books.
        """
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post("/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """
        Authenticated user can create a book.
        """
        self.authenticate()
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post("/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # ---------------- UPDATE ----------------

    def test_update_book(self):
        """
        Authenticated user can update a book.
        """
        self.authenticate()
        data = {
            "title": "Updated Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.put(
            f"/books/{self.book.id}/update/",
            data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ---------------- DELETE ----------------

    def test_delete_book(self):
        """
        Authenticated user can delete a book.
        """
        self.authenticate()
        response = self.client.delete(
            f"/books/{self.book.id}/delete/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # ---------------- FILTER / SEARCH / ORDER ----------------

    def test_filter_books_by_year(self):
        """
        Test filtering books by publication year.
        """
        response = self.client.get("/books/?publication_year=2020")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_books(self):
        """
        Test searching books by title.
        """
        response = self.client.get("/books/?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_books(self):
        """
        Test ordering books by title.
        """
        response = self.client.get("/books/?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
