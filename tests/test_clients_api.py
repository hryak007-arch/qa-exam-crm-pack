def test_create_client_success(client):
    payload = {
        "full_name": "Ілля Прядко",
        "phone": "+380501112233",
        "email": "test@example.com",
        "address": "Суми, вул. Тестова, 1"
    }
    r = client.post("/clients", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert "id" in data
    assert data["full_name"] == payload["full_name"]


def test_create_client_validation_error(client):
    # Відсутній full_name => очікуємо 422 (або 400, якщо так реалізовано)
    r = client.post("/clients", json={"phone": "+380501112233"})
    assert r.status_code in (400, 422)
