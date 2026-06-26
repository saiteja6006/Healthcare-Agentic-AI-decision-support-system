from app.services.ingestion_service import IngestionService

service = IngestionService()

service.ingest_document(
    file_path= "data/policy_documents.txt",
    collection_name = "policy_documents"
)

print("Policy documents ingested successfully")