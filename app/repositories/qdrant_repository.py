from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    Filter,
    FieldCondition,
    MatchValue
)
from qdrant_client.models import PayloadSchemaType

from app.core.config import settings

class QdrantRepository:

    def __init__(self):

        self.client = QdrantClient(
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key
        )

    def create_collection(self, collection_name):

            self.client.create_collection(
                collection_name = collection_name,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

    def store_document(
                    self,
                    collection_name,
                    document_id,
                    vector,
                    payload
            ):
                self.client.upsert(
                    collection_name = collection_name,
                    points=[
                        {
                            "id":document_id,
                            "vector": vector,
                            "payload": payload
                        }
                    ]
                )

    def create_payload_index(
                  self,
                  collection_name
    ):
           self.client.create_payload_index(
                  collection_name=collection_name,
                  field_name="modality",
                  field_schema=PayloadSchemaType.KEYWORD
           )            

    def search_documents(
                  self,
                  collection_name,
                  vector,
                  metadata_filter=None,
                  limit=3):
           
           results  = self.client.query_points(
                  collection_name=collection_name,
                  query=vector,
                  query_filter=metadata_filter,
                  limit = limit
           )
         
           return results.points        