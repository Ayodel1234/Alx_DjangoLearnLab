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

## Security Best Practices Implemented

This project applies Django security best practices to protect against
common web vulnerabilities.

### Secure Settings
- DEBUG set to False
- Browser protections enabled:
  - SECURE_BROWSER_XSS_FILTER
  - X_FRAME_OPTIONS
  - SECURE_CONTENT_TYPE_NOSNIFF
- Secure cookies enforced:
  - CSRF_COOKIE_SECURE
  - SESSION_COOKIE_SECURE

### CSRF Protection
- All POST forms include `{% csrf_token %}`

### SQL Injection Prevention
- Django ORM is used for all database queries
- User inputs are validated using Django forms

### Content Security Policy (CSP)
- CSP headers configured to restrict content loading to same origin


## HTTPS and Secure Redirects Configuration

This project enforces HTTPS to ensure secure communication
between clients and the server.

### Django HTTPS Settings
The following settings are configured in `settings.py`:
- SECURE_SSL_REDIRECT forces all HTTP requests to HTTPS
- SECURE_HSTS_SECONDS enables HTTP Strict Transport Security
- SECURE_HSTS_INCLUDE_SUBDOMAINS applies HSTS to subdomains
- SECURE_HSTS_PRELOAD allows browser preload listing
- SESSION_COOKIE_SECURE ensures session cookies are HTTPS-only
- CSRF_COOKIE_SECURE ensures CSRF cookies are HTTPS-only

### Secure Headers
Additional headers are configured to improve security:
- X_FRAME_OPTIONS = "DENY" (prevents clickjacking)
- SECURE_CONTENT_TYPE_NOSNIFF = True
- SECURE_BROWSER_XSS_FILTER = True

### Deployment Configuration (Example)
In production, HTTPS should be enabled using SSL/TLS certificates
configured in the web server (e.g., Nginx or Apache).

Example (Nginx):
- Configure SSL certificates
- Redirect HTTP (port 80) to HTTPS (port 443)

### Security Review
These measures help protect against:
- Man-in-the-middle attacks
- Session hijacking
- Clickjacking
- Cross-site scripting (XSS)

Further improvements may include automated certificate renewal
and advanced monitoring.