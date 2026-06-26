from app.services.embedding_service import EmbeddingService
from app.repositories.qdrant_repository import QdrantRepository
from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue
)


class PolicyRetrievalService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.qdrant_repository = QdrantRepository()

    def retrieve(self, query: str):

        query_vector = self.embedding_service.generate_embedding(
            query
        )  

        MIN_SCORE = 0.30

        results = self.qdrant_repository.search_documents(
            collection_name = "policy_guidelines",
            vector = query_vector,
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
            limit=5
    ):
        results  = self.client.search(
            collection_name = "policy_guidelines",
            query = vector,
            limit = limit
        )

        return results