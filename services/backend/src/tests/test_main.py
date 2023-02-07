import pytest


@pytest.mark.unit
def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}


@pytest.mark.unit
def test_scan_endpoint_response(test_app):
    response = test_app.post("/scan", json={"data": "test"})
    assert response.status_code == 200