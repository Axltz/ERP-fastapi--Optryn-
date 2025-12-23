def test_register_first_user_is_admin(client):
    response = client.post(
        "/auth/register",
        json={
            "username": "admin",
            "password": "123456"
        }
    )

    assert response.status_code == 200
    assert response.json()["role"] == "admin"

def test_register_second_user_without_admin_fails(client):
    client.post(
        "/auth/register",
        json={"username": "admin", "password": "123456"}
    )

    response = client.post(
        "/auth/register",
        json={"username": "user1", "password": "123456"}
    )

    assert response.status_code == 403
def test_admin_can_register_users(client):
    client.post(
        "/auth/register",
        json={"username": "admin", "password": "123456"}
    )

    login = client.post(
        "/auth/login",
        data={"username": "admin", "password": "123456"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    token = login.json()["access_token"]

    response = client.post(
        "/auth/register",
        json={"username": "user1", "password": "123456"},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["role"] == "user"
