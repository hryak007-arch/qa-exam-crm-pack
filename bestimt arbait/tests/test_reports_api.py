def test_report_period_ok(client):
    c = client.post("/clients", json={"full_name": "Клієнт 4", "phone": "+380500000004"}).json()
    client.post("/orders", json={"client_id": c["id"], "device": "Xiaomi", "problem": "Чистка", "price": 300})

    r = client.get("/reports/period", params={"date_from": "2026-01-01", "date_to": "2026-12-31"})
    assert r.status_code == 200
    data = r.json()
    assert "total_orders" in data and "by_status" in data

    # порожній період
    r_empty = client.get("/reports/period", params={"date_from": "2000-01-01", "date_to": "2000-01-02"})
    assert r_empty.status_code == 200
