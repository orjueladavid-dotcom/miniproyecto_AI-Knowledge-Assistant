import pytest
from app.services.assistance_service import (
    BootstrapAssistantService,
)


@pytest.mark.anyio
async def test_service_returns_answer() -> None:
    service = BootstrapAssistantService()
    result = await service.answer("¿Qué es FastAPI?")
    assert "FastAPI" in result["answer"]
    assert result["provider"] == "bootstrap-local"