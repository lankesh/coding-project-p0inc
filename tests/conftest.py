import pytest
from fastapi.testclient import TestClient

from src.db import calendar_db
from src.main import app  # Replace with your actual FastAPI app import

@pytest.fixture
def client():
    return TestClient(app)

# Fixture to reset the singleton database before each test
@pytest.fixture(autouse=True)
def reset_db():
    calendar_db.reset()  # Reset the database before each test
