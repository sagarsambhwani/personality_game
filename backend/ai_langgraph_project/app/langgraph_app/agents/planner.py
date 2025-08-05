import os
import base64
from typing_extensions import TypedDict, Annotated

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from IPython.display import Image, display
import time


# ========================
# 1. Set up Gemini model
# ========================
os.environ["GOOGLE_API_KEY"] = 

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash-preview-image-generation",
    temperature=0.8
)


# ========================
# 2. Define LangGraph State
# ========================
class State(TypedDict):
    messages: Annotated[list, add_messages]  # Conversation history
    image_base64: str  # The generated image (base64)


# ========================
# 3. LangGraph Node to Generate Image
# ========================
def generate_image_node(state: State) -> State:
    prompt = state["messages"][-1].content

    response: AIMessage = llm.invoke(
        [HumanMessage(content=prompt)],
        generation_config=dict(response_modalities=["TEXT", "IMAGE"])
    )

    # Extract image base64 from Gemini response
    def _get_image_base64(resp: AIMessage) -> str:
        try:
            image_block = next(
                block
                for block in resp.content
                if isinstance(block, dict) and block.get("image_url")
            )
            return image_block["image_url"]["url"].split(",")[-1]
        except StopIteration:
            return "NO_IMAGE_FOUND"

    image_base64 = _get_image_base64(response)

    # Add image info to messages (optional)
    system_msg = "Image generated successfully." if image_base64 != "NO_IMAGE_FOUND" else "No image was returned."

    return {
        "messages": state["messages"] + [{"role": "system", "content": system_msg}],
        "image_base64": image_base64
    }


# ========================
# 4. Build the Graph
# ========================
graph_builder = StateGraph(State)
graph_builder.add_node("generate_image", generate_image_node)
graph_builder.set_entry_point("generate_image")
graph_builder.set_finish_point("generate_image")
graph = graph_builder.compile()


# ========================
# 5. Optional: Render the Mermaid Diagram (Jupyter/IPython only)
# ========================
try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    pass


# ========================
# 6. Stream Output Loop (CLI)
# ========================
def stream_graph_updates(user_input: str):
    for event in graph.stream({
        "messages": [HumanMessage(content=user_input)],
        "image_base64": ""
    }):
        for value in event.values():
            last_msg = value["messages"][-1]["content"]
            print("Assistant:", last_msg)

            if value["image_base64"] and value["image_base64"] != "NO_IMAGE_FOUND":
                try:
                    # Show image
                    display(Image(data=base64.b64decode(value["image_base64"]), width=300))

                    # === SAVE THE IMAGE TO A FOLDER ===
                    folder = "generated_images"
                    os.makedirs(folder, exist_ok=True)

                    image_data = base64.b64decode(value["image_base64"])
                    filename = os.path.join(folder, f"image_{int(time.time())}.png")
                    with open(filename, "wb") as f:
                        f.write(image_data)
                    print(f"Image saved to {filename}")
                    
                except Exception as e:
                    print("Error displaying or saving image:", e)


# ========================
# 7. Run the chatbot
# ========================
while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except:
        # fallback for non-interactive environment
        user_input = "A scenic mountain range during sunrise"
        print("User:", user_input)
        stream_graph_updates(user_input)
        break
