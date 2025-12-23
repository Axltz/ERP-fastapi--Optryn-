from app.services.auth_service import get_current_user

def test_inventory_entry_forbidden_for_user(client, sample_product, normal_user):
    client.app.dependency_overrides[get_current_user] = lambda: normal_user

    response = client.post(
        "/inventory/entrada",
        json={
            "productID": sample_product.id,
            "quantity": 1
        }
    )

    assert response.status_code == 403


def test_inventory_entry_allowed_for_admin(client, sample_product, admin_user):
    client.app.dependency_overrides[get_current_user] = lambda: admin_user

    response = client.post(
        "/inventory/entrada",
        json={
            "productID": sample_product.id,
            "quantity": 1
        }
    )

    assert response.status_code == 200
