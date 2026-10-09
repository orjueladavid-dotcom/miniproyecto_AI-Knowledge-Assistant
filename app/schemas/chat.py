from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=2000)


class ChatResponse(BaseModel):
    answer: str
    provider: str


class InfoResponse(BaseModel):
    name: str
    version: str
    environment: str
    llm_enabled: bool