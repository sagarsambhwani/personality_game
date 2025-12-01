from langgraph.graph import StateGraph, END
from app.schemas.chat import PersonalityState
from app.langgraph_app.agents.user_profile import user_profile_node
from app.langgraph_app.agents.prompt_generation import prompt_generation_node
from app.langgraph_app.agents.image_generation import image_gen_node
from app.langgraph_app.agents.mcq_generation import mcq_node
from app.langgraph_app.agents.mbti_analysis import mbti_analyzer_node
from app.langgraph_app.agents.response import response_node

# -----------------------------
# Graph Assembly
# -----------------------------
def create_personality_graph():
    """
    Creates and compiles the personality analysis workflow graph.
    
    Returns:
        Compiled LangGraph application
    """
    workflow = StateGraph(PersonalityState)

    # Add all nodes to the graph
    workflow.add_node("user_profile", user_profile_node)
    workflow.add_node("prompt_generation", prompt_generation_node)
    workflow.add_node("image_generation", image_gen_node)
    workflow.add_node("mcq_generation", mcq_node)
    workflow.add_node("mbti_analysis", mbti_analyzer_node)
    workflow.add_node("final_response", response_node)

    # Define the workflow edges
    workflow.set_entry_point("user_profile")
    workflow.add_edge("user_profile", "prompt_generation")
    workflow.add_edge("prompt_generation", "image_generation")
    workflow.add_edge("image_generation", "mcq_generation")
    workflow.add_edge("mcq_generation", "mbti_analysis")
    workflow.add_edge("mbti_analysis", "final_response")
    workflow.add_edge("final_response", END)

    # Compile and return the graph
    return workflow.compile()

# Create the compiled graph instance
app = create_personality_graph()
