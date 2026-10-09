from fastapi import APIRouter
from app.schemas.chat import InfoResponse

router = APIRouter(tags=["Health & Info"])

@router.get("/health")
async def health_check() -> dict:
    return {"status": "ok"}

@router.get("/api/v1/info", response_model=InfoResponse)
async def get_info() -> InfoResponse:
    return InfoResponse(
        name="AI Knowledge Assistant",
        version="0.1.0",
        environment="development",
        llm_enabled=False,
    )