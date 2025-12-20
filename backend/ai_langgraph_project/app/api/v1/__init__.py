from fastapi import APIRouter
from app.api.v1.endpoint import chatbot, workflow_nodes

api_router = APIRouter()

# Include chatbot routes
api_router.include_router(chatbot.router, prefix="/personality", tags=["personality"])
api_router.include_router(workflow_nodes.router, prefix="/nodes", tags=["workflow-nodes"])
