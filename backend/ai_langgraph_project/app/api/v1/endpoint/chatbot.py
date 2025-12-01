from fastapi import APIRouter, HTTPException
from app.schemas.chat import Profile, PersonalityState
from app.langgraph_app.workflows.chatbot_graph import app as personality_app

router = APIRouter()

@router.post("/analyze")
async def analyze_personality(profile: Profile):
    """
    Analyze personality based on user profile.
    
    Args:
        profile: User demographic profile
        
    Returns:
        Complete personality analysis including MBTI result
    """
    try:
        # Create initial state with user profile
        initial_state = PersonalityState(profile=profile)
        
        # Run the graph workflow
        result = personality_app.invoke(initial_state)
        
        # Return the final response
        return {
            "status": "success",
            "profile": profile.dict(),
            "analysis": result.analysis.dict() if result.analysis else None,
            "images_generated": len(result.images),
            "mcqs_count": len(result.mcqs),
            "mbti_result": result.mbti_result,
            "final_response": result.final_response
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing personality analysis: {str(e)}")

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "personality_analysis"}
