from pathlib import Path

from app.services.pdf.reader import extract_text_from_pdf


pdf_path = Path("data/documents/academics/Aryan_Jadhav_VP_Resume.pdf")


if not pdf_path.exists():
    print(f"PDF not found: {pdf_path}")
    raise SystemExit(1)


try:
    text = extract_text_from_pdf(str(pdf_path))

    if not text.strip():
        print("PDF opened, but no text was extracted.")
    else:
        print("\nPDF successfully read!")
        print(f"Extracted characters: {len(text)}")
        print("\n--- PDF TEXT ---\n")
        print(text[:5000])

except Exception as error:
    print("\nPDF reading failed.")
    print(f"Error: {error}")