from app.services.policy_retrieval_service import(
    PolicyRetrievalService
)

service = PolicyRetrievalService()

results = service.retrieve(
    "lower back pain in 8 weeks"
)

print(results)