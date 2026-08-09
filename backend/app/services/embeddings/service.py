import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai


# Find backend/.env
BASE_DIR = Path(__file__).resolve().parents[3]
ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)


class EmbeddingService:

    def __init__(self):
        api_key = os.getenv("LLM_API_KEY")

        if not api_key:
            raise ValueError(
                f"LLM_API_KEY not found. "
                f"Please check your .env file at: {ENV_FILE}"
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = "gemini-embedding-001"

    def generate_embedding(self, text: str) -> list[float]:
        response = self.client.models.embed_content(
            model=self.model,
            contents=text
        )

        return response.embeddings[0].values


embedding_service = EmbeddingService()