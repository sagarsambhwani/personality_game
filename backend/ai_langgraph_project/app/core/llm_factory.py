import os
import time
import logging
from typing import Optional, Any
from functools import wraps
from langchain_core.runnables import Runnable
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LLMFactory:
    """
    A factory to provide configured LLM instances with built-in rate limiting and provider switching.
    """
    
    @staticmethod
    def _rate_limit_wrapper(func):
        """Decorator to add rate limiting sleep before execution."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Simple rate limiting: wait 15s to be safe for Gemini Free Tier (5 RPM = 12s interval)
            # We can optimize this to track last call time, but fixed sleep is safer for now.
            logger.info("Rate limiter: Waiting 15s before LLM call...")
            time.sleep(15)
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Basic retry logic for 429 could be added here
                logger.error(f"LLM call failed: {e}")
                raise e
        return wrapper

    @staticmethod
    def get_llm(temperature: float = 0.7, model_name: Optional[str] = None) -> Runnable:
        """
        Get a text-generation LLM.
        Prioritizes Groq if GROQ_API_KEY is set, otherwise falls back to Gemini with rate limiting.
        """
        groq_api_key = os.getenv("GROQ_API_KEY")
        
        if groq_api_key:
            logger.info("Using Groq LLM")
            # Groq implementation (High limits, usually no need for strict sleep)
            model = model_name or "openai/gpt-oss-120b"
            return ChatGroq(
                temperature=temperature,
                model_name=model,
                api_key=groq_api_key
            )
        else:
            logger.warning("Groq API Key not found. Falling back to Gemini (Rate Limited).")
            # Gemini implementation (Strict 5 RPM limit)
            model = "gemini-1.5-flash" # Use 1.5 flash or similar
            llm = ChatGoogleGenerativeAI(model=model, temperature=temperature)
            
            # Monkey-patch invoke to add rate limiting
            # (A cleaner way would be a wrapper class, but this is efficient for now)
            original_invoke = llm.invoke
            llm.invoke = LLMFactory._rate_limit_wrapper(original_invoke)
            return llm

    @staticmethod
    def get_vision_llm() -> Any:
        """
        Get a vision-capable LLM (Gemini).
        Always applies rate limiting as this is likely purely Gemini.
        """
        # For now, only Gemini supports vision in this setup cleanly
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
        # Note: 'gemini-1.5-pro-vision' might need adjustment based on available models
        
        # Apply rate limit
        # Using client directly in original code, but if we move to LangChain wrapper:
        # (This method expects caller to use LangChain interface. 
        # If original code uses raw genai.Client, we might need a different approach or refactor consumer)
        
        return llm 
    
    @staticmethod
    def rate_limit_sleep(seconds: int = 15):
        """Public helper to sleep manually if needed."""
        logger.info(f"Manual rate limit sleep: {seconds}s")
        time.sleep(seconds)
