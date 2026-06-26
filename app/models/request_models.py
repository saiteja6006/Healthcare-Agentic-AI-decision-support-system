from pydantic import BaseModel, Field, field_validator

class CaseRequest(BaseModel):

    condition: str = Field(..., min_length=1)
    duration_weeks: int = Field(..., gt=0)
    physical_therapy: bool


    @field_validator("condition")
    @classmethod
    def validate_condition(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Condition cannot be empty")
        return value