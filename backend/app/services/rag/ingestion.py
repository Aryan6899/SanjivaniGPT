from pathlib import Path

from app.services.pdf.reader import extract_text_from_pdf
from app.services.rag.text_processor import (
    clean_text,
    create_chunks
)
from app.services.embeddings.service import embedding_service
from app.services.vector_db.chroma_service import vector_db


def ingest_pdf(
    file_path: str,
    source_name: str,
    category: str = "general"
):
    """
    Read a PDF, process its text, generate embeddings,
    and store the chunks in ChromaDB.
    """

    # 1. Extract text
    text = extract_text_from_pdf(file_path)

    # 2. Clean text
    cleaned_text = clean_text(text)

    # 3. Create chunks
    chunks = create_chunks(
        cleaned_text,
        chunk_size=1000,
        overlap=200
    )

    print(f"Created {len(chunks)} chunks.")

    # 4. Process each chunk
    for index, chunk in enumerate(chunks):

        print(
            f"Processing chunk "
            f"{index + 1}/{len(chunks)}..."
        )

        # Generate embedding
        embedding = embedding_service.generate_embedding(
            chunk
        )

        # Unique ID
        document_id = (
            f"{Path(source_name).stem}_chunk_{index}"
        )

        # Metadata
        metadata = {
            "source": source_name,
            "chunk": index,
            "category": category
        }

        # Store in ChromaDB
        vector_db.add_document(
            document_id=document_id,
            text=chunk,
            embedding=embedding,
            metadata=metadata
        )

    return {
        "source": source_name,
        "chunks": len(chunks),
        "status": "success"
    }