from fastapi import APIRouter, Depends, HTTPException, Request
from app.models.settings import Settings, get_settings
from app.services.rag_service import RAGService
from app.models.request_models import QueryRequest

router = APIRouter()

def get_rag_service(request: Request, settings: Settings = Depends(get_settings)) -> RAGService:
    """Dependency to provide an instance of RAGService."""
    index = getattr(request.app, "index", None)
    if index is None:
        raise HTTPException(status_code=500, detail="Index is not initialized.")
    return RAGService(index)

@router.post("/generate")
async def generate_response(query_request: QueryRequest, rag_service: RAGService = Depends(get_rag_service)):
    """Generate a response for the given query."""
    try:
        response = rag_service.generate_response(query_request.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))