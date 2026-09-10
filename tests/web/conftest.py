import pytest
from fastapi.testclient import TestClient

from unit_converter.web.app import app


@pytest.fixture
def client():
    return TestClient(app)
