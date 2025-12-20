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
         print("PGVECTOR_CONN not set. Using pure LLM fallback.")
         # Fallback to pure LLM analysis
         llm = LLMFactory.get_llm(temperature=0.3)
         
         answers_summary = "\n".join(
             [f"Q: {mcq['question']}\nA: {mcq.get('answer', 'Not answered')}" for mcq in state.mcqs]
         )
         
         prompt = f"""
         You are an MBTI personality analyst.
         Here are the user's MCQ answers (based on visual scenarios):
         {answers_summary}

         Analyze these answers to determine the user's most likely MBTI type.
         Since we don't have the reference guide available, rely on general MBTI theory.
         
         Respond with ONLY the MBTI type (e.g., INTJ, ENFP) and a short explanation (2–3 lines).
         """
         
         try:
             response = llm.invoke(prompt)
             state.mbti_result = response.content
         except Exception as e:
             state.mbti_result = f"Error in fallback analysis: {str(e)}"
             
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
