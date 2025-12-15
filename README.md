OPTRYN BACKEND (ERP – FASTAPI)

Professional backend for inventory management with authentication, role-based access control, and automated testing.


OVERVIEW

Optryn is an ERP-style backend focused on inventory control.
It is designed following solid software engineering principles to ensure stability,
security, and maintainability.

This project represents a real backend system, not a tutorial or a school exercise.


KEY FEATURES

- JWT-based authentication
- Role-based access control (admin, user)
- Inventory management with business rules
- Clean architecture (routes, services, models, schemas)
- Automated tests using pytest
- Isolated test database


ARCHITECTURE

The backend follows a layered architecture:

- Routes handle HTTP requests
- Services contain business logic
- Models define database entities
- Schemas validate and serialize data

This separation improves maintainability and scalability.


TESTING

The project includes automated tests covering:

- Authentication
- Authorization and roles
- Inventory operations
- Product management

Tests run against an isolated SQLite database to avoid affecting real data.

Run tests with:

pytest -v


PROJECT STATUS

Current version: Backend v1.0

- Core business logic implemented
- Authentication and permissions stable
- Tests passing
- Ready for CI integration


NEXT STEPS

- Continuous Integration (GitHub Actions)
- Test coverage reporting
- Inventory movement history
- Reporting and filtering
- Role expansion
