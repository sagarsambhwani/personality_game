from app.schemas.chat import PersonalityState

def response_node(state: PersonalityState) -> PersonalityState:
    """Generate final response"""
    state.final_response = {"result": f"Your MBTI personality analysis result:\n\n{state.mbti_result}"}
    return state
