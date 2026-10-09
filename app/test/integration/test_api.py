from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_info() -> None:
    response = client.get("/api/v1/info")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "AI Knowledge Assistant"
    assert data["llm_enabled"] is False


def test_chat_valid_question() -> None:
    response = client.post(
        "/api/v1/chat",
        json={"question": "¿Qué es FastAPI?"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert data["provider"] == "bootstrap-local"


def test_chat_invalid_question_too_short() -> None:
    response = client.post(
        "/api/v1/chat",
        json={"question": "hi"},
    )
    assert response.status_code == 422