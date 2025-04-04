# backend

# Django Backend with RESTful API

This project is a Django-based backend providing a RESTful API using the Django REST Framework (DRF).

---

## Features

- RESTful API with Django REST Framework
- Token-based Authentication (JWT / Session / Customizable)
- PostgreSQL / SQLite (configurable)
- CORS support for frontend integration
- Modular structure for apps

---

## Requirements

Make sure you have the following installed:
- Python 3.8+
- pip / pipenv / poetry
- Git

---

## Installation & Setup

### Clone the Repository

```bash
https://github.com/Talai-Next/backend.git
```

### Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root (if used), or update `settings.py` for:

```env
DATABASE_URL=your-database-url
DJANGO_SECRET_KEY=your-secret-key
```

### Apply Migrations

```bash
python manage.py migrate
```


### Run Development Server

```bash
python manage.py runserver
```

Your API will be available at: [http://localhost:8000/](http://localhost:8000/)



## Project Structure (Example)

```
├── api/
│   ├── migrations/
│   ├── serializers/
│   ├── tests/
│   ├── views/
│   └── urls.py
├── backend/
│   ├── settings.py
│   ├── urls.py
├── manage.py
├── requirements.txt
├── .gitignore
└── .env
```


---

## Useful Commands

```bash
python manage.py runserver          # Start dev server
python manage.py makemigrations    # Create migrations
python manage.py migrate           # Apply migrations
python manage.py createsuperuser   # Create admin user
```

---

## License

This project is licensed under the MIT License.
