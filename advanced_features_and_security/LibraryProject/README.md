# LibraryProject

This project is part of the ALX Django Learn Lab.

## Objective
To set up a Django development environment and run the Django development server.

## How to Run
python manage.py runserver


## Permissions and Groups Setup

This project uses Django's built-in permissions and groups system
to control access to Book-related actions.

### Custom Permissions
Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

### Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

### Enforcement
Permissions are enforced in views using Django's
`@permission_required` decorator.

Example:
@permission_required("relationship_app.can_edit", raise_exception=True)

## Permissions and Groups Setup

This project demonstrates role-based access control using
Django permissions and groups.

### Custom Permissions
Defined in `bookshelf/models.py`:
- can_view
- can_create
- can_edit
- can_delete

### Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

### Enforcement
Permissions are enforced in `bookshelf/views.py` using Django’s
`@permission_required` decorator with `raise_exception=True`.

Example:
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()