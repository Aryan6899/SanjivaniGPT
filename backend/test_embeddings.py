from app.services.embeddings.service import embedding_service


text = """
Sanjivani University Academic Calendar 2026-27.
The academic calendar contains important dates for students,
including semester examinations, holidays, and academic activities.
"""


embedding = embedding_service.generate_embedding(text)


print("Embedding generated successfully!")
print("Vector dimensions:", len(embedding))
print("First 10 values:")
print(embedding[:10])