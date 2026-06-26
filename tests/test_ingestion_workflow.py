from app.services.ingestion_service import IngestionService
import os

service = IngestionService()

clinical_folder = "data/clinical_guidelines"

for file_name in os.listdir(
        clinical_folder):

    service.ingest_document(
        f"{clinical_folder}/{file_name}",
        "clinical_guidelines"
    )


policy_folder = "data/policy_documents"

for file_name in os.listdir(
        policy_folder):

    service.ingest_document(
        f"{policy_folder}/{file_name}",
        "policy_guidelines"
    )



print("Ingestion done successfully")