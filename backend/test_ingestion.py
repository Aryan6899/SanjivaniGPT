from app.services.rag.ingestion import ingest_pdf


pdf_path = (
    "data/documents/academics/"
    "Aryan_Jadhav_VP_Resume.pdf"
)


result = ingest_pdf(
    file_path=pdf_path,
    source_name="Aryan_Jadhav_VP_Resume.pdf",
    category="academics"
)


print("\n" + "=" * 50)
print("INGESTION RESULT")
print("=" * 50)

print(result)