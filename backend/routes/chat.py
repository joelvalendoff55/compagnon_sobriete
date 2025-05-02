from fastapi import APIRouter
from models.message import Message
from backend.services.openai_service import get_openai_response

router = APIRouter()

@router.post("/chat")
def chat_with_companion(msg: Message):
    reply = get_openai_response(msg.user_message)
    return {"response": reply}

