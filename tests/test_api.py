def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "environment" in data
    assert "health" in data

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["database"] == "connected"

def test_info_endpoint(client):
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert "app_name" in data
    assert "version" in data
    assert "environment" in data

def test_crud_item_flow(client):
    # 1. Create item
    payload = {
        "title": "K3s Worker Node",
        "description": "2 vCPU / 2GB RAM Worker Node VM",
        "price": 15.50,
        "is_active": True
    }
    create_res = client.post("/api/v1/items/", json=payload)
    assert create_res.status_code == 201
    item = create_res.json()
    assert item["title"] == "K3s Worker Node"
    item_id = item["id"]

    # 2. Read item by ID
    get_res = client.get(f"/api/v1/items/{item_id}")
    assert get_res.status_code == 200
    assert get_res.json()["title"] == "K3s Worker Node"

    # 3. Read list of items
    list_res = client.get("/api/v1/items/")
    assert list_res.status_code == 200
    assert len(list_res.json()) >= 1

    # 4. Update item
    update_payload = {"price": 19.99, "description": "Updated Node Specs"}
    put_res = client.put(f"/api/v1/items/{item_id}", json=update_payload)
    assert put_res.status_code == 200
    assert put_res.json()["price"] == 19.99
    assert put_res.json()["description"] == "Updated Node Specs"

    # 5. Delete item
    del_res = client.delete(f"/api/v1/items/{item_id}")
    assert del_res.status_code == 204

    # 6. Verify item is deleted
    get_deleted = client.get(f"/api/v1/items/{item_id}")
    assert get_deleted.status_code == 404
