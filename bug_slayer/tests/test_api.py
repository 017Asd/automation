import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Bug, TestCase, BugSeverity, BugStatus

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Bug Slayer API"}

def test_create_bug():
    bug_data = {
        "title": "Test Bug",
        "description": "This is a test bug",
        "severity": BugSeverity.HIGH,
        "status": BugStatus.OPEN
    }
    response = client.post("/api/bugs/", json=bug_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == bug_data["title"]
    assert data["severity"] == bug_data["severity"]

def test_get_bugs():
    response = client.get("/api/bugs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_test_case():
    test_case_data = {
        "name": "Test Case 1",
        "description": "This is a test case",
        "input_data": {"param1": "value1"},
        "expected_output": {"result": "success"}
    }
    response = client.post("/api/test-cases/", json=test_case_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_case_data["name"]
    assert data["input_data"] == test_case_data["input_data"]

def test_generate_edge_cases():
    test_case_data = {
        "name": "Test Case 1",
        "description": "This is a test case",
        "input_data": {"param1": 100},
        "expected_output": {"result": "success"}
    }
    response = client.post("/api/test-cases/generate-edge-cases", json=test_case_data)
    assert response.status_code == 200
    data = response.json()
    assert "edge_cases" in data
    assert isinstance(data["edge_cases"], list)

def test_invalid_bug_data():
    invalid_bug_data = {
        "title": "Test Bug",
        # Missing required fields
    }
    response = client.post("/api/bugs/", json=invalid_bug_data)
    assert response.status_code == 422  # Validation error

def test_nonexistent_bug():
    response = client.get("/api/bugs/nonexistent-id")
    assert response.status_code == 404 