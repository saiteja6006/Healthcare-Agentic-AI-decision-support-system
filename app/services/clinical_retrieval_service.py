from app.services.embedding_service import EmbeddingService
from app.repositories.qdrant_repository import QdrantRepository
from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue
)


class RetrievalService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.qdrant_repository = QdrantRepository()

    def retrieve(self, query: str):

        query_vector = self.embedding_service.generate_embedding(
            query
        )  

        MIN_SCORE = 0.40

        metadata_filter = Filter(
            must=[
                FieldCondition(
                    key="modality",
                    match=MatchValue(
                        value="MRI"
                    )
                )
            ]
        )

        results = self.qdrant_repository.search_documents(
            collection_name= "clinical_guidelines",
            vector = query_vector,
            metadata_filter=metadata_filter,
            limit = 3
        
        )  

        filtered_results = []


        for point in results:
            if point.score >= MIN_SCORE:
                filtered_results.append(
                    point.payload["text"]
                )   

        return filtered_results
    
    def search_documents(
            self,
            vector,
            limit=3
    ):
        results  = self.client.search(
            collection_name = "clinical_guidelines",
            query = vector,
            limit = limit
        )

        return results
        