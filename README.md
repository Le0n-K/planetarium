# Planetarium Service API

This is a Django REST Framework application for managing a planetarium service. It provides APIs for handling astronomy shows, reservations, tickets, and more.

## Features

- Manage planetarium domes, show themes, and astronomy shows
- Schedule show sessions
- Handle ticket reservations
- User authentication
- API documentation with Swagger and ReDoc

## Technologies

- Django
- Django REST Framework
- PostgreSQL (for production)
- SQLite (for development)
- Docker and Docker Compose
- drf-spectacular for API documentation

## Setup

### Local Development

1. Clone the repository:
```shell
git clone https://github.com/Le0n-K/planetarium.git
cd planetarium
```
2. Create a virtual environment and activate it:
```shell
python -m venv venv
venv\Scripts\activate  (for Windows)
source/venv/bin/activate   (for Mac)
```
3. Install dependencies:
```shell
pip install -r requirments.txt
```
4. Run migrations:
```shell
python manage.py migrate
```
5. Start the development server:
```shell
python manage.py runserver
```

### Docker Setup

1. Make sure you have Docker and Docker Compose installed.

2. Build and run the containers:
```shell
docker-compose build
docker-compose up
```


The application will be available at `http://localhost:8001`.

## API Documentation

Once the server is running, you can access the API documentation:

- Swagger UI: `http://localhost:8000/api/doc/swagger/`
- ReDoc: `http://localhost:8000/api/doc/redoc/`

## Environment Variables

The project uses environment variables for configuration. Create a `.env` file in the project root with the following variables:

```shell
SECRET_KEY=SECRET_KEY
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
POSTGRES_DB=planetarium
POSTGRES_USER=planetarium
POSTGRES_PASSWORD=planetarium
POSTGRES_HOST=db
POSTGRES_PORT=5433
```