# AI-Powered Personality & MBTI Analysis Pipeline

This project implements an advanced **AI-driven personality assessment pipeline** using **LangGraph**, **Google Gemini**, and **Vector Search**. It takes a user's demographic profile and takes them through a multi-step generative journey—creating personalized visual scenarios, generating psychological questions based on those visuals, and finally determining their MBTI personality type using a knowledge base.

## 🚀 Project Overview

The system operates as a stateful graph workflow where data flows through several intelligent nodes:

1.  **Profile Analysis**: Analyzes user demographics to determine stylistic cues (tone, themes).
2.  **Creative Prompt Generation**: Generates imaginative scenarios/story prompts tailored to the user's profile.
3.  **Image Generation**: Uses **Gemini 2.5 Flash** to generate unique images based on the creative prompts.
4.  **Visual MCQ Generation**: Uses **Gemini Vision** to analyze the generated images and create personality-testing Multiple Choice Questions (MCQs).
5.  **MBTI Analysis**: Analyzes the user's (simulated) answers against an MBTI knowledge base using **PGVector** and **Semantic Search** to determine the personality type.

## 🛠️ Tech Stack

-   **Orchestration**: [LangGraph](https://langchain-ai.github.io/langgraph/) (StateGraph)
-   **LLMs & Vision**: Google Gemini (`gemini-1.5-pro`, `gemini-2.5-flash-image-preview`, `gemini-1.5-pro-vision`)
-   **Data Validation**: Pydantic v2
-   **Vector Database**: PostgreSQL with `pgvector`
-   **Framework**: LangChain (Google GenAI integrations)

## 🧩 Workflow Nodes

The pipeline consists of the following nodes:

| Node | Function | Model Used |
| :--- | :--- | :--- |
| **`user_profile`** | Analyzes demographics to extract style cues & summary. | `gemini-1.5-pro` |
| **`prompt_generation`** | Creates 3-5 visual prompts based on style cues. | `gemini-1.5-pro` |
| **`image_generation`** | Generates actual images from prompts and saves locally. | `gemini-2.5-flash-image-preview` |
| **`mcq_generation`** | Analyzes images to generate decision-making MCQs. | `gemini-1.5-pro-vision` |
| **`mbti_analysis`** | Matches answers to MBTI types using vector search. | `gemini-1.5-pro` + `embedding-001` |

## 📋 Prerequisites

-   Python 3.9+
-   Google Cloud API Key (with access to Gemini models)
-   PostgreSQL database with `pgvector` extension installed
-   Environment variables set up

## ⚙️ Setup & Installation

1.  **Clone the repository**
    ```bash
    git clone <repository-url>
    cd ai_langgraph_project
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    *Ensure you have `langgraph`, `langchain-google-genai`, `pydantic`, `psycopg2-binary` (or equivalent), and `google-generativeai`.*

3.  **Environment Variables**
    Create a `.env` file:
    ```env
    GOOGLE_API_KEY=your_google_api_key
    PGVECTOR_CONN=postgresql+psycopg://user:pass@localhost:5432/mbti
    ```

4.  **Database Setup**
    Ensure your PostgreSQL instance is running and the `mbti_docs` collection is populated with MBTI reference material for the vector search to work.

## 🏃‍♂️ Usage

### Running the API Server

1. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your GOOGLE_API_KEY and PGVECTOR_CONN
   ```

2. **Start the FastAPI server**
   ```bash
   python -m uvicorn app.main:app --reload
   ```
   
   The API will be available at `http://localhost:8000`
   
3. **Access the API documentation**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### API Endpoints

#### POST `/api/v1/personality/analyze`
Analyze personality based on user profile.

**Request Body:**
```json
{
  "name": "Sagar",
  "age": 25,
  "gender": "Male",
  "profession": "Data Engineer",
  "nationality": "Indian"
}
```

**Response:**
```json
{
  "status": "success",
  "profile": {...},
  "analysis": {...},
  "images_generated": 3,
  "mcqs_count": 3,
  "mbti_result": "INTJ - ...",
  "final_response": {...}
}
```

#### GET `/api/v1/personality/health`
Health check endpoint for the personality service.

### Testing the Pipeline

Run the test script to verify the setup:
```bash
python test_pipeline.py
```

## 📂 Output

-   **Images**: Generated images are saved in the `outputs/` directory.
-   **Final Result**: A structured MBTI analysis and explanation.

## 🔮 Future Enhancements

-   Interactive frontend (Streamlit/React) to collect real-time user answers.
-   More complex branching logic in LangGraph based on user choices.
-   Enhanced vector knowledge base for deeper psychological insights.
