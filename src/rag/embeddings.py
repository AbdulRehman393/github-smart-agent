from langchain_core.embeddings import Embeddings
from openai import OpenAI
from src.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, EMBEDDING_MODEL


class OpenRouterEmbeddings(Embeddings):
    """Custom embeddings class for OpenRouter with LangChain compatibility."""

    def __init__(self):
        self.client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=OPENROUTER_BASE_URL
        )
        self.model = EMBEDDING_MODEL

    def embed_documents(self, texts):
        embeddings = []
        for text in texts:
            response = self.client.embeddings.create(
                model=self.model,
                input=text
            )
            embeddings.append(response.data[0].embedding)
        return embeddings

    def embed_query(self, text):
        response = self.client.embeddings.create(
            model=self.model,
            input=text
        )
        return response.data[0].embedding


def get_embeddings():
    return OpenRouterEmbeddings()