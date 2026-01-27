def test_create_order_success(client):
    # створюємо клієнта
    c = client.post("/clients", json={"full_name": "Клієнт 1", "phone": "+380500000001"}).json()

    payload = {
        "client_id": c["id"],
        "device": "iPhone 11",
        "problem": "Не заряджається",
        "price": 1200
    }
    r = client.post("/orders", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["client_id"] == c["id"]
    assert data["status"] == "new"


def test_get_orders_filter_by_status(client):
    c = client.post("/clients", json={"full_name": "Клієнт 2", "phone": "+380500000002"}).json()
    o1 = client.post("/orders", json={"client_id": c["id"], "device": "Dell", "problem": "Діагностика"}).json()

    client.put(f"/orders/{o1['id']}/status", json={"new_status": "done"})

    r = client.get("/orders", params={"status": "done"})
    assert r.status_code == 200
    assert all(i["status"] == "done" for i in r.json())


def test_change_status_creates_log(client):
    c = client.post("/clients", json={"full_name": "Клієнт 3", "phone": "+380500000003"}).json()
    o = client.post("/orders", json={"client_id": c["id"], "device": "Samsung", "problem": "Заміна екрана"}).json()

    r = client.put(f"/orders/{o['id']}/status", json={"new_status": "in_progress"})
    assert r.status_code == 200

    details = client.get(f"/orders/{o['id']}").json()
    assert details["status"] == "in_progress"
    assert len(details.get("status_log", [])) >= 1
