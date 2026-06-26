from app.agents.intake_agent import IntakeAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.supervisor_agent import SupervisorAgent

from pprint import pprint


patient_case = {
    "condition": "Neck pain",
    "duration_weeks": 15,
    "physical_therapy": False
}

intake_agent = IntakeAgent()
decision_agent = DecisionAgent()
supervisor_agent = SupervisorAgent()

print("\n=== INTAKE AGENT ===")
case_data = intake_agent.execute(patient_case)
print(case_data)


print("\n=== DECISION AGENT ===")
decision_result = (
    decision_agent.execute(
        case_data
    )
)

print(decision_result)

print(
    "\n=== TOOLS USED ==="
)

print(
    decision_result[
        "tools_used"
    ]
)

print("\n=== Supervisor AGENT ===")

supervisor_result=(
    supervisor_agent.execute(
        decision_result
    )
)

print(supervisor_result)


