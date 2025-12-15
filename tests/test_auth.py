def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={
            "username": "newuser",
            "password": "123456"
        }
    )
    assert response.status_code == 200
    assert response.json()["username"] == "newuser"


def test_login_user(client):
    client.post(
        "/auth/register",
        json={
            "username": "loginuser",
            "password": "123456"
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "loginuser",
            "password": "123456"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
