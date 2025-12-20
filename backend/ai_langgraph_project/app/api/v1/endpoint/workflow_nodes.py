from fastapi import APIRouter, HTTPException
from app.schemas.chat import PersonalityState
from app.langgraph_app.agents.user_profile import user_profile_node
from app.langgraph_app.agents.prompt_generation import prompt_generation_node
from app.langgraph_app.agents.image_generation import image_gen_node
from app.langgraph_app.agents.mcq_generation import mcq_node
from app.langgraph_app.agents.mbti_analysis import mbti_analyzer_node

router = APIRouter()

@router.post("/user-profile")
async def run_user_profile(state: PersonalityState):
    """Execution step 1: Analyze User Profile"""
    try:
        return user_profile_node(state)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in user_profile_node: {str(e)}")

@router.post("/prompt-generation")
async def run_prompt_generation(state: PersonalityState):
    """Execution step 2: Generate Image Prompts"""
    try:
        return prompt_generation_node(state)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in prompt_generation_node: {str(e)}")

@router.post("/image-generation")
async def run_image_generation(state: PersonalityState):
    """Execution step 3: Generate Images"""
    try:
        return image_gen_node(state)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in image_gen_node: {str(e)}")

@router.post("/mcq-generation")
async def run_mcq_generation(state: PersonalityState):
    """Execution step 4: Generate MCQs from Images"""
    try:
        return mcq_node(state)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in mcq_node: {str(e)}")

@router.post("/mbti-analysis")
async def run_mbti_analysis(state: PersonalityState):
    """Execution step 5: Analyze MBTI"""
    try:
        return mbti_analyzer_node(state)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in mbti_analyzer_node: {str(e)}")
