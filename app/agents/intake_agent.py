from app.agents.base_agent import BaseAgent

class IntakeAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Intake Agent"
            )
        
    def execute(
                self,
                patient_case
        ):
            return {
                "condition":
                patient_case.get("condition"),

                "duration_weeks":
                patient_case.get("duration_weeks"),

                "physical_therapy":
                patient_case.get("physical_therapy")
            }