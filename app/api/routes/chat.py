from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.assistance_service import AssistanceService

router = APIRouter(prefix="/api/v1", tags=["Chat & Assistant"])

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest) -> ChatResponse:
    answer, provider = AssistanceService.answer_question(request.question)
    return ChatResponse(answer=answer, provider=provider)