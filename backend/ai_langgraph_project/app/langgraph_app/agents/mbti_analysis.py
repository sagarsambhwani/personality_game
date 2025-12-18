import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.core.llm_factory import LLMFactory
from langchain_community.vectorstores import PGVector
from app.schemas.chat import PersonalityState

def mbti_analyzer_node(state: PersonalityState) -> PersonalityState:
    """Analyze MCQ answers using MBTI knowledge base (pgvector + Gemini)"""

    CONNECTION_STRING = os.getenv("PGVECTOR_CONN")  # e.g. postgresql+psycopg://user:pass@localhost:5432/mbti
    COLLECTION_NAME = "mbti_docs"
    
    if not CONNECTION_STRING:
         print("PGVECTOR_CONN environment variable not set. Skipping vector search.")
         # Fallback or error handling here
         return state

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    try:
        vectorstore = PGVector(
            connection_string=CONNECTION_STRING,
            collection_name=COLLECTION_NAME,
            embeddings=embeddings,
        )
        retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

        answers_summary = "\n".join(
            [f"Q: {mcq['question']}\nA: {mcq.get('answer', 'Not answered')}" for mcq in state.mcqs]
        )

        docs = retriever.get_relevant_documents(answers_summary)
        context = "\n\n".join([d.page_content for d in docs])

        llm = LLMFactory.get_llm(temperature=0.3)

        prompt = f"""
        You are an MBTI personality analyst.  
        Here are the user's MCQ answers:  
        {answers_summary}  

        Using the MBTI guide context, identify the most likely MBTI type.  
        Respond with ONLY the MBTI type (e.g., INTJ, ENFP) and a short explanation (2–3 lines).  

        Context from MBTI guide:  
        {context}
        """

        response = llm.invoke(prompt)
        state.mbti_result = response.content
    except Exception as e:
        print(f"Error in MBTI analysis: {e}")
        state.mbti_result = {"error": str(e)}

    return state
