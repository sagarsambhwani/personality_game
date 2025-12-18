from app.core.llm_factory import LLMFactory
from app.schemas.chat import PersonalityState, GeneratedPrompts

def prompt_generation_node(state: PersonalityState) -> PersonalityState:
    """
    Generate 3-5 story/image prompts using Gemini LLM based on profile analysis.
    """
    if state.analysis is None:
        raise ValueError("Profile analysis missing in state")

    llm = LLMFactory.get_llm(temperature=0.7)
    
    # Force structured output to ensure we get a list of prompts
    structured_llm = llm.with_structured_output(GeneratedPrompts)

    summary = state.analysis.summary
    style_cues = state.analysis.style_cues
    tone = style_cues.tone
    themes = ", ".join(style_cues.themes)
    visual_hints = ", ".join(style_cues.visual_hints)

    prompt_text = (
        "You are an imaginative story and image prompt generator. "
        "Based on the user's short description and style cues, generate 3-5 creative, visually rich prompts suitable for image generation. "
        "Do NOT include any personal data, just create imaginative scenarios.\n\n"
        f"User summary: {summary}\n"
        f"Style cues: tone={tone}, themes={themes}, visual hints={visual_hints}"
    )

    # Invoke Gemini LLM to get structured prompts
    result: GeneratedPrompts = structured_llm.invoke(prompt_text)

    # Save into state
    state.image_prompts = result
    return state
