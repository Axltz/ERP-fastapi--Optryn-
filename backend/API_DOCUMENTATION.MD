OPTRYN API DOCUMENTATION


GENERAL DESCRIPTION

This API provides backend services for inventory management.
It enforces authentication, authorization, and business rules
to ensure data integrity and controlled access.


AUTHENTICATION

The API uses JSON Web Tokens (JWT).

Authentication flow:
1. User registers
2. User logs in
3. API returns a JWT token
4. Token is sent in the Authorization header for protected requests

Authorization header format:

Authorization: Bearer <token>


ROLES AND PERMISSIONS

Available roles:

- admin
  - Can create products
  - Can modify inventory
  - Can perform stock adjustments

- user
  - Can view products
  - Cannot modify inventory

Access control is enforced at the route level using dependencies.


CORE MODULES


AUTH MODULE

Responsible for:
- User registration
- User login
- Token generation
- Password validation


PRODUCT MODULE

Responsibilities:
- Create products (admin only)
- List products
- Validate product data


INVENTORY MODULE

Responsibilities:
- Stock entry
- Stock removal
- Inventory adjustment
- Permission validation for inventory operations


DATA VALIDATION

All incoming data is validated using schemas.
Invalid or malformed requests are rejected automatically.


ERROR HANDLING

- Unauthorized access returns HTTP 401
- Forbidden actions return HTTP 403
- Validation errors return HTTP 422

This ensures consistent API behavior.


TESTING STRATEGY

The API is fully testable using pytest.
Tests verify both business logic and permission rules.

Test database is isolated and recreated for each test run.


API STABILITY

This API is considered stable for version 1.0.
Future versions may extend functionality without breaking existing behavior.
