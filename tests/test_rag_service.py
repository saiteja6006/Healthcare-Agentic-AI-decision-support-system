from app.services.rag_service import RAGService

service = RAGService()

response = service.ask(
    "Can MRI be approved for liver cancer staging?"
)

print("\nANSWER:\n")
print(response)