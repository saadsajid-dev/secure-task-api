import uuid

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def register_and_login():
    email = f"user_{uuid.uuid4()}@example.com"
    password = "testpassword"

    client.post(
        "/register",
        json={
            "email": email,
            "password": password
        }
    )

    response = client.post(
        "/login",
        data={
            "username": email,
            "password": password
        }
    )

    token = response.json()["access_token"]
    return token

def test_tasks_requires_auth():
    response = client.get("/tasks")
    assert response.status_code == 401

def test_create_task_with_auth():
    token = register_and_login()

    response = client.post(
        "/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Test Task",
            "description": "Testing"
        }
    )

    assert response.status_code == 201
    data = response.json()

    assert data["title"] == "Test Task"
    assert data["description"] == "Testing"

def test_user_cannot_access_another_users_task():
    token_a = register_and_login()

    create_response = client.post(
        "/tasks",
        headers={"Authorization": f"Bearer {token_a}"},
        json={
            "title": "Private Task",
            "description": "User A task"
        }
    )

    task_id = create_response.json()["id"]

    token_b = register_and_login()

    response = client.put(
        f"/tasks/{task_id}",
        headers={"Authorization": f"Bearer {token_b}"},
        json={
            "title": "Hacked",
            "description": "Should fail"
        }
    )

    assert response.status_code == 404

def test_task_pagination():
    token = register_and_login()

    for i in range(3):
        client.post(
            "/tasks",
            headers={"Authorization": f"Bearer {token}"},
            json={
                "title": f"Task {i}",
                "description": "Pagination test"
            }
        )

    response = client.get(
        "/tasks?skip=0&limit=2",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 2
