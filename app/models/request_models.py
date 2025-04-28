from pydantic import BaseModel
from typing import List, Optional

class QueryRequest(BaseModel):
    query: str
    top_k: Optional[int] = 5

class DocumentRequest(BaseModel):
    documents: List[str]

class RetrievalRequest(BaseModel):
    query_request: QueryRequest
    document_request: DocumentRequest