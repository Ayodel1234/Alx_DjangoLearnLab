from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from api.models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API CRUD operations and permissions.
    """

    def setUp(self):
        """
        Set up test data before each test.
        This uses a separate test database automatically.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)

        self.author = Author.objects.create(name="Test Author")

        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

    def authenticate(self):
        """
        Helper method to authenticate requests using token.
        """
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )

    def test_list_books(self):
        """
        Test retrieving list of books (read-only access).
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

    def test_create_book_requires_authentication(self):
        """
        Test that creating a book without authentication is denied.
        """
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post("/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_with_authentication(self):
        """
        Test creating a book with authentication.
        """
        self.authenticate()
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post("/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        """
        Test updating a book.
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

    def test_delete_book(self):
        """
        Test deleting a book.
        """
        self.authenticate()
        response = self.client.delete(
            f"/books/{self.book.id}/delete/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
