from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

class EmbeddingService:

    @staticmethod
    def generate_embedding(text: str):
        return model.encode(text).tolist()
    