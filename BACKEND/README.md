# TiketiTamashaKE

TiketiTamashaKE is a Django-based backend for managing events and ticketing in Kenya. It includes features like JWT authentication, OTP verification, QR code generation, and Swagger API documentation.

## Features

- Custom user model with roles (USER, EVENT_MANAGER, ADMIN).
- JWT authentication and OTP-based login.
- Event management for event managers.
- Ticket purchasing with QR code generation.
- Swagger API documentation.
- Dockerized setup with PostgreSQL, Redis, and Celery.

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed.
- Python 3.11+ installed (for local development).

### Environment Variables

Copy the `.env.example` file to `.env` and update the values as needed:

```bash
cp .env.example .env
```

### Running the Project

1. Build and start the Docker containers:

```bash
docker-compose up --build
```

2.Apply migrations

```bash
docker-compose exec web python manage.py migrate
```

3.Create a superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```

4.Access the application:

- API: `http://localhost:8000`
- Swagger Documentation: `http://localhost:8000/swagger/`
- Admin Panel: `http://localhost:8000/admin/`

### Additional Commands

- Run tests:

```bash
docker-compose exec web python manage.py test
```

- Access the Django shell:

```bash
docker-compose exec web python manage.py shell
```

## License

This project is licensed under the MIT License.
