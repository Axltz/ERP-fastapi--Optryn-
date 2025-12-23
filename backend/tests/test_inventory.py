from app.services.auth_service import get_current_user

def test_inventory_entry_admin(client, sample_product, admin_user):
    client.app.dependency_overrides[get_current_user] = lambda: admin_user

    response = client.post(
        "/inventory/entrada",
        json={
            "productID": sample_product.id,
            "quantity": 5
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Stock increased successfully"


def test_inventory_entry_user_forbidden(client, sample_product, normal_user):
    client.app.dependency_overrides[get_current_user] = lambda: normal_user

    response = client.post(
        "/inventory/entrada",
        json={
            "productID": sample_product.id,
            "quantity": 5
        }
    )

    assert response.status_code == 403


def test_inventory_exit_admin(client, sample_product, admin_user):
    client.app.dependency_overrides[get_current_user] = lambda: admin_user

    response = client.post(
        "/inventory/salida",
        json={
            "productID": sample_product.id,
            "quantity": 3
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Stock decreased successfully"


def test_inventory_adjust_admin(client, sample_product, admin_user):
    client.app.dependency_overrides[get_current_user] = lambda: admin_user

    response = client.post(
        "/inventory/ajuste",
        json={
            "productID": sample_product.id,
            "new_stock": 20
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Stock adjusted successfully"
