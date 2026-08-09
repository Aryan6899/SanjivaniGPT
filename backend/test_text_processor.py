from app.services.pdf.reader import extract_text_from_pdf
from app.services.rag.text_processor import (
    clean_text,
    create_chunks
)


pdf_path = "data/documents/academics/Aryan_Jadhav_VP_Resume.pdf"


# Step 1: Extract PDF text
text = extract_text_from_pdf(pdf_path)

print("Original characters:", len(text))


# Step 2: Clean text
cleaned_text = clean_text(text)

print("Cleaned characters:", len(cleaned_text))


# Step 3: Create chunks
chunks = create_chunks(
    cleaned_text,
    chunk_size=1000,
    overlap=200
)

print("Number of chunks:", len(chunks))


# Display first 3 chunks
for index, chunk in enumerate(chunks[:3], start=1):

    print("\n" + "=" * 60)
    print(f"CHUNK {index}")
    print("=" * 60)

    print(chunk)