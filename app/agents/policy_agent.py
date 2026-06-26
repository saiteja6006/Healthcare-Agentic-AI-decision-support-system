import json

from app.agents.base_agent import BaseAgent
from app.services.policy_retrieval_service import (
  PolicyRetrievalService
) 
from app.services.llm_service import (
    LLMService
)


class PolicyAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Policy Agent"
            )
        self.policy_retrieval_service = (
            PolicyRetrievalService()
        )
        self.llm_service=(
            LLMService()
        )
    

    def execute(self, case_data):
        query = (
            f"{case_data['condition']}"
            f"{case_data['duration_weeks']} weeks"
        )

        results = (
            self.policy_retrieval_service.retrieve(
                query
            )
        )
        
        policy_evidence = []
        for point in results.points:
            policy_evidence.append(
                point.payload["text"]
            )

        
        policy_text = "\n".join(
            policy_evidence
        )

        prompt = f"""
        You are a helathcare policy review agent.

        Patient Condition:
        {case_data['condition']}
        
        Duration:
        {case_data['duration_weeks']}
        
        Policy Evidence:
        {policy_text}

        Return ONLY valid JSON.

        {{
            "policy_match": true,
            "policy_reasoning": 
                    "Explaination",

            "policy_confidence":
                "HIGH | MEDIUM | LOW"        
        }}
        """
        response = (
            self.llm_service.generate_response(
                prompt
            )
        )

        try:
            policy_result = (
                json.loads(response)
            )
        except Exception:
            policy_result = {
                "policy_match": False,
                "policy_reasoning": 
                    "Unable to parse model response",
                "policy_confidence":
                     "LOW"    
            }  

            policy_result["policy_evidence"] = policy_evidence  
        return policy_result