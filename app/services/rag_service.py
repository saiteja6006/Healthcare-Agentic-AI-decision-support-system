from app.services.retrieval_service import RetrievalService
from app.services.llm_service import LLMService

class RAGService:

    def __init__(self):
        self.retreival_service = RetrievalService()
        self.llm_service = LLMService()


    def ask(self, question:str):
        results = self.retreival_service.retrieve(
            question
        )    

        context = "\n\n".join([
            point.payload["text"]
            for point in results.points
        ])

        prompt = f"""
You are a healthcare assistant.
Use only the provided context.
Context:
{context}

Question:
{question}

Answer:
"""
        
        return self.llm_service.generate_response(
            prompt
        )