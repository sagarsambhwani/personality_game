from google import genai
from app.schemas.chat import PersonalityState

def mcq_node(state: PersonalityState) -> PersonalityState:
    """Analyze images with Gemini Vision and generate MCQs"""
    
    client = genai.Client()
    state.mcqs = []

    for image_path in state.images:
        print(f"Generating MCQ for image: {image_path}")

        try:
            with open(image_path, "rb") as f:
                image_bytes = f.read()

            response = client.models.generate_content(
                model="gemini-1.5-pro-vision",
                contents=[
                    {
                        "role": "user",
                        "parts": [
                            {"text": "Analyze this image and create a multiple-choice question "
                                     "that tests the viewer's decision-making or personality. "
                                     "Provide 4 distinct answer options."},
                            {"inline_data": {"mime_type": "image/png", "data": image_bytes}}
                        ]
                    }
                ],
            )

            if response.candidates and response.candidates[0].content.parts:
                mcq_text = response.candidates[0].content.parts[0].text
                lines = mcq_text.split("\n")
                question = lines[0]
                options = [line.strip("1234. ") for line in lines[1:] if line.strip()]

                state.mcqs.append({"question": question, "options": options})
            else:
                print(f"No MCQ generated for image: {image_path}")
        
        except Exception as e:
            print(f"Error generating MCQ for image '{image_path}': {e}")

    return state
