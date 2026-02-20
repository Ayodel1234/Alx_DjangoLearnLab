# Social Media API

## Setup

1. Install dependencies
pip install django djangorestframework

2. Run migrations
python manage.py migrate

3. Start server
python manage.py runserver

## Endpoints

POST /api/register/
POST /api/login/
GET /api/profile/

Authentication uses Token Authentication.
Include token in header:

Authorization: Token <your_token>
