def test_home(test_client):
    response = test_client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "Welcome to the Home Page" in response.text


def test_users(test_client):
    response = test_client.get("/users")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "Welcome to the Users Page" in response.text


def test_items(test_client):
    response = test_client.get("/items")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "Welcome to the Items Page" in response.text
