from app.utils.llama_index_helper import create_index, load_index
from llama_index.core import VectorStoreIndex
class RAGService:
    def __init__(self, index: VectorStoreIndex):
        """Initialize the RAG service by loading or creating an index."""
        self.index = index
        self.query_engine = self.index.as_query_engine()

    def generate_response(self, query: str) -> str:
        """Generate a response for the given query using the query engine."""
        return self.query_engine.query(query)