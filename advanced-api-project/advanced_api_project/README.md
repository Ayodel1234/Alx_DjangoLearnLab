## Book API – Generic Views

This project demonstrates the use of Django REST Framework generic views
to implement CRUD operations on the Book model.

### Views
- BookListView: Lists all books (public access)
- BookDetailView: Retrieves a single book by ID (public access)
- BookCreateView: Creates a new book (authenticated users only)
- BookUpdateView: Updates an existing book (authenticated users only)
- BookDeleteView: Deletes a book (authenticated users only)

### Permissions
Read-only endpoints are open to all users.
Create, update, and delete operations require authentication.

### Validation
Custom validation ensures publication_year is not set in the future.


## Testing

This project uses Django REST Framework’s APITestCase
to test Book API endpoints.

### Covered Tests
- List and retrieve books
- Create, update, and delete books
- Authentication and permission enforcement
- Filtering, searching, and ordering

### Run Tests
```bash
python manage.py test api
