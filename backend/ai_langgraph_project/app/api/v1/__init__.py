from fastapi import APIRouter
from app.api.v1.endpoint import chatbot

api_router = APIRouter()

# Include chatbot routes
api_router.include_router(chatbot.router, prefix="/personality", tags=["personality"])
