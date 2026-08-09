from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.get("/test")
def chat_test():
    return {
        "message": "Chat API is working"
    }