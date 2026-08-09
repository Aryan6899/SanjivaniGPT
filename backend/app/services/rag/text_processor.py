import re


def clean_text(text: str) -> str:
    """
    Clean extracted PDF text.
    """

    # Replace multiple spaces/tabs with one space
    text = re.sub(r"[ \t]+", " ", text)

    # Reduce excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove spaces at the beginning/end of lines
    text = "\n".join(
        line.strip()
        for line in text.splitlines()
    )

    return text.strip()


def create_chunks(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 200
) -> list[str]:
    """
    Split text into overlapping chunks.
    """

    if not text:
        return []

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start += chunk_size - overlap

    return chunks