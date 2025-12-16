"""
Test script to verify the personality pipeline setup
"""
from app.schemas.chat import Profile, PersonalityState
from app.langgraph_app.workflows.chatbot_graph import app as personality_app
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_pipeline():
    """Test the personality analysis pipeline"""
    
    # Create a test profile
    test_profile = Profile(
        name="Sagar",
        age=25,
        gender="Male",
        profession="Data Engineer",
        nationality="Indian"
    )
    
    print("=" * 50)
    print("Testing Personality Analysis Pipeline")
    print("=" * 50)
    print(f"\nProfile: {test_profile.dict()}\n")
    
    try:
        # Create initial state
        initial_state = PersonalityState(profile=test_profile)
        
        # Run the pipeline
        print("Running pipeline...")
        result = personality_app.invoke(initial_state)
        
        print("\n✓ Pipeline completed successfully!")
        print(f"\nAnalysis Summary: {result.analysis.summary if result.analysis else 'N/A'}")
        print(f"Images Generated: {len(result.images)}")
        print(f"MCQs Created: {len(result.mcqs)}")
        print(f"\nMBTI Result: {result.mbti_result}")
        print(f"\nFinal Response: {result.final_response}")
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_pipeline()
