import requests
import json
import sys

BASE_URL = "http://localhost:8000/api/v1/nodes"

# Initial Profile Data
initial_state = {
    "profile": {
        "name": "Sagar",
        "age": 25,
        "gender": "Male",
        "profession": "Data Engineer",
        "nationality": "Indian"
    },
    # Initialize other fields to empty defaults or None as required by the schema
    "images": [],
    "mcqs": []
}

headers = {'Content-Type': 'application/json'}

def run_step(step_name, endpoint, input_state):
    print(f"\n--- Running Step: {step_name} ({endpoint}) ---")
    url = f"{BASE_URL}/{endpoint}"
    try:
        response = requests.post(url, headers=headers, json=input_state)
        if response.status_code == 200:
            print(f"✓ {step_name} Success")
            return response.json()
        else:
            print(f"✗ {step_name} Failed: {response.status_code}")
            print(response.text)
            sys.exit(1)
    except Exception as e:
        print(f"✗ Error connecting to {endpoint}: {e}")
        sys.exit(1)

def test_flow():
    state = initial_state
    
    # 1. User Profile Node
    state = run_step("User Profile Analysis", "user-profile", state)
    print(f"  Summary: {state.get('analysis', {}).get('summary', 'N/A')[:50]}...")

    # 2. Prompt Generation Node
    state = run_step("Prompt Generation", "prompt-generation", state)
    prompts = state.get('image_prompts', {}).get('prompts', [])
    print(f"  Generated {len(prompts)} prompts")

    # 3. Image Generation Node
    # Note: This might take time
    state = run_step("Image Generation", "image-generation", state)
    images = state.get('images', [])
    print(f"  Generated {len(images)} images: {images}")

    # 4. MCQ Generation Node
    state = run_step("MCQ Generation", "mcq-generation", state)
    mcqs = state.get('mcqs', [])
    print(f"  Generated {len(mcqs)} MCQs")

    # 5. MBTI Analysis Node
    state = run_step("MBTI Analysis", "mbti-analysis", state)
    mbti = state.get('mbti_result')
    print(f"  MBTI Result: {mbti}")

    print("\n✓ Full Node-by-Node Flow Verified!")

if __name__ == "__main__":
    test_flow()
