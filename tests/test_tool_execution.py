import json

from openai import OpenAI

from app.core.config import settings

from app.tools.clinical_tool import (
    retrieve_clinical_evidence
)

from app.tools.policy_tool import (
    retrieve_policy_evidence
)

client = OpenAI(
    api_key=settings.openai_api_key
)

tools = [

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

messages = [

    {
        "role": "user",

        "content":
            "Find clinical evidence for lower back pain."
    }
]

response = client.chat.completions.create(

    model="gpt-4.1-mini",

    messages=messages,

    tools=tools
)

message = (
    response
    .choices[0]
    .message
)

tool_call = (
    message.tool_calls[0]
)

tool_name = (
    tool_call.function.name
)

arguments = json.loads(
    tool_call.function.arguments
)

query = (
    arguments["query"]
)

print("\n=== TOOL SELECTED ===")
print(tool_name)

print("\n=== QUERY ===")
print(query)



if tool_name == "retrieve_clinical_evidence":

    tool_result = (
        retrieve_clinical_evidence(
            query
        )
    )

elif tool_name == "retrieve_policy_evidence":

    tool_result = (
        retrieve_policy_evidence(
            query
        )
    )

else:

    raise ValueError(
        f"Unknown tool: {tool_name}"
    )

print("\n=== TOOL RESULT ===")

for item in tool_result:

    print(item)



messages.append(message)

messages.append({

    "role": "tool",

    "tool_call_id":
        tool_call.id,

    "content":
        "\n".join(tool_result)
})

final_response = (
    client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=messages,

        tools=tools
    )
)

print("\n=== FINAL ANSWER ===")

print(
    final_response
    .choices[0]
    .message
    .content
)