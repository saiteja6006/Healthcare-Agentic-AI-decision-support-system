from app.agents.base_agent import BaseAgent

from app.services.tool_calling_service import (
    ToolCallingService
)



class DecisionAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Decision Agent"
            )
        self.tool_service = (
            ToolCallingService()
        )
  
        
        
    def execute(self, workflow_data):

        condition = (
            workflow_data["condition"]
        )

        duration_weeks = (
            workflow_data["duration_weeks"]
        )

        physical_therapy = (
            workflow_data["physical_therapy"]
        )

        prompt = f"""
You are a healthcare utilization review agent.

Patient Condition:
{condition}

Duration:
{duration_weeks} weeks

Physical Therapy Completed:
{physical_therapy}

Rules:

1. The evidence must explicitly support the user's condition.

2. The evidence must discuss the same condition
   or body part.

3. Similar symptoms are NOT enough.

4. Generic MRI guidance is NOT enough.

5. If evidence discusses a different condition,
   different disease, or different body part,
   return NO.

Examples:

User Condition: Eye Tumor
Evidence: Neck pain MRI guideline
Result: NO

User Condition: Arm Pain
Evidence: Lumbar MRI guideline
Result: NO

User Condition: Neck Pain
Evidence: Neck pain MRI guideline
Result: YES

Return ONLY valid JSON.
{{
     "recommendation": ""

     "reasoning": ""

     "confidence": ""
}}
Do not return markdown.
Do not return explanations.
Do not return code fences.
Return JSON only.
"""
        tool_results = (
            self.tool_service.execute(
                prompt
            )
        )

        print("\n===== TOOL RESULTS =====")
        print(tool_results)
        print("========================\n")

        return {

    "recommendation":
        tool_results[
            "recommendation"
        ],

    "reasoning":
        tool_results[
            "reasoning"
        ],

    "confidence":
        tool_results[
            "confidence"
        ],

    "tools_used":
        tool_results[
            "tool_names"
        ],

    "evidence":
        tool_results[
            "tool_results"
        ],

    "grounding_failed":
        tool_results[
            "grounding_failed"
        ]
}