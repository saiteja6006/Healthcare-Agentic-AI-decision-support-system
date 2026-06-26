from app.repositories.qdrant_repository import QdrantRepository

repo = QdrantRepository()

repo.create_collection(
    "clinical_guidelines")

repo.create_collection(
    "policy_guidelines"
)

repo.create_payload_index(
    "clinical_guidelines"
)

repo.create_payload_index(
    "policy_guidelines"
)


print("Collection created successfully")