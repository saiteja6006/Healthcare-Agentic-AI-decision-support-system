from app.agents.base_agent import BaseAgent


class SupervisorAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            name="Supervisor Agent"
        )

    def execute(
            self,
            workflow_data):

        decision = (
            workflow_data.get(
                "decision"
            )
        )

        tools_used = (
            workflow_data.get(
                "tools_used",
                []
            )
        )

        evidence = (
            workflow_data.get(
                "evidence",
                []
            )
        )

        if not decision:

            return {

                "status":
                    "REVIEW REQUIRED",

                "reason":
                    "Decision missing"
            }
        grounding_failed = (
            workflow_data.get(
                "grounding_failed",
                False
            )
        )

        if grounding_failed:
            return {
                "status":
                   "REVIEW REQUIRED",
                   "reason":
                      "Evidence validation failed"
            }

        if not evidence:

            return {

                "status":
                    "REVIEW REQUIRED",

                "reason":
                    "Evidence missing"
            }
        
        
        

        if (
            "retrieve_clinical_evidence"
            not in tools_used
        ):

            return {

                "status":
                    "REVIEW REQUIRED",

                "reason":
                    "Clinical evidence missing"
            }

        if (
            "retrieve_policy_evidence"
            not in tools_used
        ):

            return {

                "status":
                    "REVIEW REQUIRED",

                "reason":
                    "Policy evidence missing"
            }

        return {

            "status":
                "VERIFIED",

            "reason":
                "Clinical and policy evidence validated"
        }
        