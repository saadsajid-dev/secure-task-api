import pytest
import uuid

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_user_registration():
    unique_email = f"testuser_{uuid.uuid4()}@example.com"
    response = client.post(
        "/register",
        json={
            "email": unique_email,
            "password": "testpassword"
        }
    )

    assert response.status_code == 200
    data = response.json()

    assert "id" in data
    assert data["email"] == unique_email

def test_user_login():
    client.post(
        "/register",
        json={
            "email": "loginuser@example.com",
            "password": "loginpassword"
        }
    )

    response = client.post(
        "/login",
        data={
            "username": "loginuser@example.com",
            "password": "loginpassword"
        }
    )

    assert response.status_code == 200
    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"
