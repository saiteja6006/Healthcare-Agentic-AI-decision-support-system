from app.services.clinical_retrieval_service import (
    RetrievalService
)

def retrieve_clinical_evidence(
        query:str
):
    retrieval_service = (
        RetrievalService()
    )

    return (
        retrieval_service.retrieve(
            query
        )
    )

   