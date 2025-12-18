from app.core.llm_factory import LLMFactory
from app.schemas.chat import PersonalityState, ProfileAnalysis

def user_profile_node(state: PersonalityState) -> PersonalityState:
    """
    Lightweight analysis from demographics → generate cues for story/image prompts.
    Uses structured LLM output (Pydantic v2) to guarantee schema compliance.
    """
    if state.profile is None:
        raise ValueError("profile missing in state")

    # Load Gemini LLM
    llm = LLMFactory.get_llm(temperature=0.4)

    # Wrap with structured output enforcement
    structured_llm = llm.with_structured_output(ProfileAnalysis)

    # Demographics
    profile_text = (
        f"Name: {state.profile.name}\n"
        f"Age: {state.profile.age}\n"
        f"Gender: {state.profile.gender}\n"
        f"Profession: {state.profile.profession}\n"
        f"Nationality: {state.profile.nationality}\n"
    )

    # Prompt instruction
    prompt = (
        "Analyze the given demographics and return a short personality sketch. "
        "Focus on descriptive cues for relatable story/image generation, not deep psychology.\n\n"
        f"User profile:\n{profile_text}"
    )

    # Get structured response
    analysis: ProfileAnalysis = structured_llm.invoke(prompt)

    # Save into state
    state.analysis = analysis
    return state
