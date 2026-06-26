from openai import OpenAI
from app.core.config import settings
import json

class EvidenceValidation:

    def __init__(self):
        
        self.client = OpenAI(
            api_key=settings.openai_api_key
        )

    def validate(
            self,
            query,
            evidence
    ):
        prompt = f"""

You are a healthcare evidence validator.

User Query:
{query}

Retrieved Evidence:
{evidence}

Your task is to determine whether the retrieved evidence is sufficient to support answering the user's request.

Rules:

1. Return YES if the evidence discusses the SAME condition or a direct clinical match.

2. Return YES if the evidence clearly supports the requested recommendation.

3. Return NO if the evidence discusses a different disease, body part, or unrelated condition.

4. Return NO if the evidence is too generic to justify the recommendation.

Examples:

User:
Neck Pain

Evidence:
Neck pain may result from muscle strain.
MRI is indicated after six weeks.

Answer:
YES

--------------------

User:
Lower Back Pain

Evidence:
MRI is indicated after six weeks of persistent lower back pain.

Answer:
YES

--------------------

User:
Eye Tumor

Evidence:
Neck pain guideline.

Answer:
NO

--------------------

User:
Arm Pain

Evidence:
Lumbar MRI guideline.

Answer:
NO

Answer ONLY:

YES

or

NO

    """
        


        response = (
            self.client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        ) 

        content=(
            response
            .choices[0]
            .message
            .content
            .strip()
        )
        return content
        