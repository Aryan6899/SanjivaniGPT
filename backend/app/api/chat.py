from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm.service import llm_service


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    message: str


@router.post("/")
def chat(request: ChatRequest):

    response = llm_service.generate(
        request.message
    )

    return {
        "reply": response
    }


@router.get("/test")
def chat_test():
    return {
        "message": "Chat API is working"
    }