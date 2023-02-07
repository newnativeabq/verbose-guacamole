from fastapi.testclient import TestClient
import pytest

from app.main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here
