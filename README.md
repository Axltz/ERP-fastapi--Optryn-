# ERP FastAPI – Optryn

## 📌 Description
Backend ERP system developed with FastAPI for managing users, products, and inventory.
The system includes JWT-based authentication, role-based access control (RBAC), and secure password handling, designed following best practices for scalable backend architectures.

This project is intended as a production-oriented backend, not a demo, and focuses on clean architecture, security, and testability.

## 🧱 Architecture
The project follows a modular and layered architecture, separating concerns clearly:

- FastAPI
- SQLAlchemy
- JWT
- Argon2
- Pytest
- GitHub Actions (CI)

Key architectural concepts:

Dependency Injection

Repository pattern

Separation of routers, services, and models

Environment-based configuration

## 🚀 Installation

1. Clone the repository:
2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

3. Install dependencies:
pip install -r requirements.txt
4. Configure environment variables:
Create a .env file and define:

DATABASE_URL

SECRET_KEY

ALGORITHM

ACCESS_TOKEN_EXPIRE_MINUTES

5. Run the application:

uvicorn app.main:app --reload


## 🔐 Authentication

The system uses JWT authentication with the following features:

Secure login with hashed passwords (Argon2)

Access tokens for authenticated requests

Role-based authorization (e.g. admin, user)

Protected routes using FastAPI dependencies

Token expiration and validation

This approach allows the backend to remain stateless, scalable, and suitable for microservices.

## 📦 Features
User management (create, update, delete)

Secure authentication and authorization

Role and permission control

Product management

Inventory tracking

Relational database design with foreign keys

Input validation and error handling

Modular and extensible structure

Planned / expandable features:

Sales and order management

Reports and analytics

Supplier management

REST integration with frontend clients

## 🧪 Tests

The project includes automated tests written with Pytest:

Unit tests for core logic

API endpoint testing

Authentication and authorization tests

Database interaction validation

Tests are executed automatically using GitHub Actions on each push and pull request, ensuring code quality and stability.

## 🧑‍💻 Autor
Axel Guillermo Martinez Martinez
Full-Stack Developer
Focused on scalable systems, clean architecture, and secure API design.
