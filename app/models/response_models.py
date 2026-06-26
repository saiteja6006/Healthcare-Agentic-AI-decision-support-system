from pydantic import BaseModel

class DecisionResponse(BaseModel):
    recommendation: str

    reasoning: str

    confidence: str

    status: str

    reason: str

    evidence: list[str]

    tools_used: list[str]