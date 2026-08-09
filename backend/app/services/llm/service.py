from google import genai

from app.config import LLM_API_KEY
from app.prompts.system import SYSTEM_PROMPT


class LLMService:

    def __init__(self):
        if not LLM_API_KEY:
            raise ValueError("LLM_API_KEY is not configured.")

        self.client = genai.Client(
            api_key=LLM_API_KEY
        )

    def generate(self, message: str) -> str:

        prompt = f"""
{SYSTEM_PROMPT}

User message:
{message}
"""

        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text


llm_service = LLMService()