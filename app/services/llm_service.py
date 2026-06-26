from openai import OpenAI
from app.core.config import settings

class LLMService:

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.openai_api_key
        )

    def generate_response(
                self,
                prompt:str):
            response = self.client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role":"user",
                        "content": prompt
                    }
                ]
            )
            
            return response.choices[0].message.content