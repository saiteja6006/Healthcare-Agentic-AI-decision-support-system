from app.services.embedding_service import EmbeddingService
from app.repositories.qdrant_repository import  QdrantRepository


class IngestionService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.qdrant_repository = QdrantRepository()

    def ingest_document(self, file_path: str, collection_name):
        with open(file_path, "r", encoding = "utf-8") as file:
            content = file.read()

        chunks = content.split("\n\n")

        for index, chunk in enumerate(chunks):
            vector = self.embedding_service.generate_embedding(chunk)

            if "clinical" in collection_name:
             payload = {
                "text":
                    chunk,
                
                "modality":
                   "MRI",
                
                "body_part":
                    "lumbar",
                
                "document_type":
                    "clinical_guidelines",
                
                "speciality":
                    "radiology",
                
                "source":
                   "clinical"
                
                }
            elif "policy" in collection_name:

               payload = {
                  
                  "text":
                    chunk,
                
                "modality":
                   "MRI",
                
                "body_part":
                    "lumbar",
                
                "document_type":
                    "policy_guidelines",
                
                "source":
                   "insurance"
                
               }

            self.qdrant_repository.store_document(
                collection_name= collection_name,
                document_id=index,
                vector=vector,
                payload=payload
            ) 
           