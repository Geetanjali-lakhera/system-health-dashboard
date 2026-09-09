from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "DOWN"


def test_version():
    client = app.test_client()

    response = client.get("/version")

    assert response.status_code == 200
    assert response.json["version"] == "1.0.0"


def test_environment():
    client = app.test_client()

    response = client.get("/environment")

    assert response.status_code == 200


def test_status():
    client = app.test_client()

    response = client.get("/status")

    assert response.status_code == 200
    assert response.json["status"] == "DOWN"


def test_metrics():
    client = app.test_client()

    response = client.get("/metrics")

    assert response.status_code == 200