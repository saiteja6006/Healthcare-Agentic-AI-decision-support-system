from app.agents.intake_agent import IntakeAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.supervisor_agent import SupervisorAgent


class DecisionService:

    def __init__(self):
        self.intake_agent = IntakeAgent()
        self.decision_agent = DecisionAgent()
        self.supervisor_agent = SupervisorAgent()

    def make_decision(
            self,
            condition,
            duration_weeks,
            physical_therapy
    ):
        case_data = {
            "condition": condition,
            "duration_weeks": duration_weeks,
            "physical_therapy": physical_therapy
        }    

        intake_result = (
            self.intake_agent.execute(
                case_data
            )
        )

        decision_result = (
            self.decision_agent.execute(
                intake_result
            )
        )


        workflow_data = {
             "decision":
                decision_result["recommendation"],

             "tools_used":
                decision_result["tools_used"],

            "evidence":
                decision_result["evidence"],

            "grounding_failed":
                 decision_result["grounding_failed"]
}
        supervisor_result=(
            self.supervisor_agent.execute(
                workflow_data
            )
        )

        return {

    "recommendation":
        decision_result[
            "recommendation"
        ],

    "reasoning":
        decision_result[
            "reasoning"
        ],

    "confidence":
        decision_result[
            "confidence"
        ],

    "status":
        supervisor_result[
            "status"
        ],

    "reason":
        supervisor_result[
            "reason"
        ],

    "evidence":
        decision_result[
            "evidence"
        ],

    "tools_used":
        decision_result[
            "tools_used"
        ]
}