from pathlib import Path

import chromadb


BASE_DIR = Path(__file__).resolve().parents[3]

CHROMA_PATH = BASE_DIR / "data" / "vector_store"


class ChromaService:

    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=str(CHROMA_PATH)
        )

        self.collection = self.client.get_or_create_collection(
            name="sanjivanigpt_documents"
        )

    def add_document(
        self,
        document_id: str,
        text: str,
        embedding: list[float],
        metadata: dict
    ):
        """
        Store one document chunk in ChromaDB.
        """

        self.collection.add(
            ids=[document_id],
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata]
        )

    def search(
        self,
        embedding: list[float],
        top_k: int = 5
    ):
        """
        Search for the most relevant document chunks.
        """

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )

        return results


vector_db = ChromaService()