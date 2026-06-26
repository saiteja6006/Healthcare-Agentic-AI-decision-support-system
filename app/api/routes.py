from fastapi import APIRouter

from app.models.request_models import CaseRequest
from app.models.response_models import DecisionResponse

from app.services.decision_service import DecisionService

router =  APIRouter()

@router.get("/")

def root():
    return {
        "message": "Healthcare Agentic AI Platform running"
    }

@router.get("/health")
def health():
    return {
        "status": "healthy"
    }

decision_service = DecisionService()

@router.post(
             "/decision",
             response_model=DecisionResponse
             )
def make_decision(
    request: CaseRequest
):
    result = decision_service.make_decision(
            condition=request.condition,
            duration_weeks=request.duration_weeks,
            physical_therapy=request.physical_therapy
        )
    return result
