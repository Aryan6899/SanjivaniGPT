from app.services.embeddings.service import embedding_service
from app.services.vector_db.chroma_service import vector_db


test_text = "Aryan_Jadhav_VP_Resume.pdf"


# Generate a real Gemini embedding
test_embedding = embedding_service.generate_embedding(
    test_text
)


vector_db.add_document(
    document_id="test_chunk_001",
    text=test_text,
    embedding=test_embedding,
    metadata={
        "source": "test_document.pdf",
        "page": 1,
        "category": "test"
    }
)


print("Document stored successfully!")

print(
    "Embedding dimensions:",
    len(test_embedding)
)

print(
    "Total documents:",
    vector_db.collection.count()
)