from app.services.clinical_retrieval_service import RetrievalService

service = RetrievalService()

results = service.retrieve(
    "When should MRI be approved for liver cancer?"
)

print(results)