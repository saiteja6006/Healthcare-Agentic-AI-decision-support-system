from app.agents.base_agent import BaseAgent
from app.services.clinical_retrieval_service import RetrievalService


class ClincialEvidenceAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Clincial Evidence Agent"
            )
        self.retrieval_service = (
            RetrievalService()
        )

    def execute(self, case_data):

        query = (
            f"{case_data['condition']}"
           f"{case_data['duration_weeks']} weeks"
        )

        results = (
            self.retrieval_service.retrieve(
                query
            )
        )

        evidence = []

        for point in results.points:
            evidence.append(
                point.payload["text"]
            )

            return{
                "evidence": evidence
            }