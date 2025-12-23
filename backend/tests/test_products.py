from app.services.auth_service import get_current_user


def test_create_product_admin(client, admin_user):
    client.app.dependency_overrides[get_current_user] = lambda: admin_user

    response = client.post(
        "/products/",
        json={
            "name": "Laptop",
            "price": 1500.0,
            "stockAvailable": 5,
            "stockMinimum":2
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"


def test_create_product_forbidden_user(client, normal_user):
    client.app.dependency_overrides[get_current_user] = lambda: normal_user

    response = client.post(
        "/products/",
        json={
            "name": "Mouse",
            "price": 20.0,
            "stockAvailable": 10,
            "stockMinimum": 4
        }
    )

    assert response.status_code == 403


def test_list_products(client, admin_user):
    client.app.dependency_overrides[get_current_user] = lambda: admin_user

    response = client.get("/products/")
    assert response.status_code == 200
