import json

from openai import OpenAI

from app.core.config import settings

from app.tools.clinical_tool import (
    retrieve_clinical_evidence
)

from app.tools.policy_tool import (
    retrieve_policy_evidence
)

from app.services.evidence_validation_service import (
    EvidenceValidation
)


class ToolCallingService:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.openai_api_key
        )

        self.tools = [

            {
                "type": "function",

                "function": {

                    "name":
                        "retrieve_clinical_evidence",

                    "description":
                        "Retrieve clinical guidelines and medical evidence.",

                    "parameters": {

                        "type": "object",

                        "properties": {

                            "query": {

                                "type": "string"
                            }
                        },

                        "required":
                            ["query"]
                    }
                }
            },

            {
                "type": "function",

                "function": {

                    "name":
                        "retrieve_policy_evidence",

                    "description":
                        "Retrieve insurance policy requirements.",

                    "parameters": {

                        "type": "object",

                        "properties": {

                            "query": {

                                "type": "string"
                            }
                        },

                        "required":
                            ["query"]
                    }
                }
            }
        ]

    def execute(
            self,
            user_prompt: str):

        messages = [

            {
                "role": "user",

                "content": user_prompt
            }
        ]

        response = (
            self.client.chat.completions.create(

                model="gpt-4.1-mini",

                messages=messages,

                tools=self.tools
            )
        )

        message = (
            response
            .choices[0]
            .message
        )

        if not message.tool_calls:

            return {

                "tool_name": None,

                "query": None,

                "tool_result": [],

                "final_answer":
                    message.content
            }

        messages.append(
            {
                "role": "assistant",
                "tool_calls": [
                    {
                    "id": tc.id,
                    "type": tc.type,
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments
                    }
                    }
                    for tc in message.tool_calls
                ]
            }
        )

        tool_names = []
        tool_results = []
        clinical_results = []
        policy_results = []

        for tool_call in message.tool_calls:
            tool_name = (
                tool_call.function.name
            )

            tool_names.append(
                tool_name
            )

            arguments = json.loads(
                tool_call.function.arguments
            )

            query = (
                arguments["query"]
            )

            print(
                f"\n Executing Tool: {tool_name}"
            )

            print(
                f"Query: {query}"
            )

            if tool_name == (
                "retrieve_clinical_evidence"
            ):
                
                result = (
                    retrieve_clinical_evidence(
                        query
                    )
                )

                clinical_results.extend(
                    result
                )
            elif tool_name == (
                "retrieve_policy_evidence"
            ):

                result = (
                    retrieve_policy_evidence(
                        query
                    )
                ) 
                if result:

                    policy_results.extend(
                    result
                )  
            else:
                raise ValueError(
                    f"Unknown tool: {tool_name}"
                )   

            tool_results.extend (
                    result
            )
            messages.append(
                {
            "role": "tool",

            "tool_call_id":
                tool_call.id,

            "content":
                "\n".join(result)
        } 
        )
            
         #Evidence Sufficiency gaurdrail


        if (
            len(clinical_results) == 0
            or
            len(policy_results) == 0
        ):
            return {

    "recommendation":
        "MANUAL REVIEW",

    "reasoning":
        """
        Insufficient clinical or policy evidence
        was found to support a recommendation.
        """,

    "confidence":
        "LOW",

    "tool_names":
        tool_names,

    "tool_results":
        [],

    "grounding_failed":
        True
}
        
        evidence_validation = (
            EvidenceValidation()
        )

        grounding_result = (
            evidence_validation.validate(
                user_prompt,
                tool_results
            )
        )




        if grounding_result!= "YES":
           return {

                "recommendation":
                "MANUAL REVIEW",
                "reasoning":
                    """
                Evidence does not sufficiently
                support the user query.
                """,

                "confidence":
                "LOW",

                 "tool_names":
                     tool_names,

                "tool_results":
                    tool_results,

                "grounding_failed":
                    True
   }
             

        final_response = (

            self.client.chat.completions.create(

                model="gpt-4.1-mini",

                messages=messages,

                tools=self.tools
            )
        )

        final_answer = (

            final_response
            .choices[0]
            .message
            .content
        )

        json_data = json.loads(
            final_answer
        )

        return {
            "recommendation":
                json_data[
                    "recommendation"
                ],
            "reasoning":
                json_data[
                      "reasoning"
                    ],

            "confidence":
                json_data[
                     "confidence"
                    ],    

            "tool_names":
                tool_names,

            "tool_results":
                tool_results,

            "final_answer":
                final_answer,
            "grounding_failed":
                False    
        }