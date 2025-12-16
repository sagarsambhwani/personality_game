from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field

# -----------------------------
# State Schema
# -----------------------------
class Profile(BaseModel):
    name: str
    age: int
    gender: str
    profession: str
    nationality: str

class StyleCues(BaseModel):
    tone: str = Field(..., description="e.g., 'futuristic, adventurous'")
    themes: List[str] = Field(..., description="List of thematic elements")
    visual_hints: List[str] = Field(..., description="Visual styling cues")

#  Define structured schema with Pydantic v2
class ProfileAnalysis(BaseModel):
    summary: str = Field(
        ...,
        description="1–2 sentence description of the person based on demographics"
    )
    style_cues: StyleCues = Field(
        ...,
        description="Stylistic cues for generating relatable story/image prompts"
    )

# Define schema for LLM-generated prompts
class GeneratedPrompts(BaseModel):
    prompts: List[str] = Field(..., description="List of 3-5 image/story prompts for the user")

# --- Core state that flows through LangGraph ---
class PersonalityState(BaseModel):
    profile: Optional[Profile] = None                     # Raw user profile
    analysis: Optional[ProfileAnalysis] = None            # Structured analysis
    image_prompts: Optional[GeneratedPrompts] = None      # Prompts for image generation
    images: List[str] = []                                # Generated image paths
    mcqs: List[Dict[str, Any]] = []                       # Generated MCQs
    mbti_result: Optional[Dict[str, Any]] = None          # Structured MBTI result
    final_response: Optional[Dict[str, Any]] = None       # Final narrative/feedback
