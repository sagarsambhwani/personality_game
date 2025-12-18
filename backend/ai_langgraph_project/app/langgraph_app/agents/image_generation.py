import os
from google import genai
from app.core.llm_factory import LLMFactory
from app.schemas.chat import PersonalityState

def image_gen_node(state: PersonalityState) -> PersonalityState:
    """Generate images using Gemini and save locally"""
    
    os.makedirs("outputs", exist_ok=True)
    client = genai.Client()

    state.images = []
    
    # Ensure image_prompts is available
    if not state.image_prompts:
        print("No image prompts found in state.")
        return state

    for i, prompt in enumerate(state.image_prompts.prompts): # Accessing prompts list from GeneratedPrompts object
        print(f"Generating image for prompt: {prompt}")

        # Rate limit before call
        LLMFactory.rate_limit_sleep(30)

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-image-preview",
                contents=[prompt],
            )
            
            if response.candidates and response.candidates[0].content.parts:
                for part in response.candidates[0].content.parts:
                    if part.inline_data is not None:
                        image_bytes = part.inline_data.data
                        file_path = f"outputs/mbti_image_{i+1}.png"
                        with open(file_path, "wb") as f:
                            f.write(image_bytes)
                        state.images.append(file_path)
            else:
                print(f"No content generated for prompt: {prompt}")

        except Exception as e:
             print(f"Error generating image for prompt '{prompt}': {e}")

    return state
