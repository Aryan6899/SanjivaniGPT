import pymupdf


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from all pages of a PDF file.
    """

    document = pymupdf.open(file_path)

    text = []

    for page in document:
        page_text = page.get_text()

        if page_text:
            text.append(page_text)

    document.close()

    return "\n".join(text)