from app.services.policy_retrieval_service import (
    PolicyRetrievalService
)


def retrieve_policy_evidence(
        query:str
):
    
    retrieval_service = (
        PolicyRetrievalService()
    )

    return (
        retrieval_service.retrieve(
            query
        )
    )   