from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.endpoints import router as api_router
from app.models.settings import get_settings
from app.utils.llama_index_helper import create_index, load_index
from app.utils.hash_util import compute_directory_hash, load_stored_hash, save_hash
import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events."""
    index = None  
    settings = get_settings()

    # Ensure the storage directory exists
    os.makedirs(settings.STORAGE_DIRECTORY, exist_ok=True)

    # Compute the current hash of the data directory
    current_hash = compute_directory_hash(settings.DATA_DIRECTORY)
    stored_hash = load_stored_hash(settings.HASH_FILE)

    # Load or create the index based on the hash
    if current_hash != stored_hash:
        print("Changes detected in the data directory. Rebuilding the index...")
        index = create_index(settings)
        save_hash(settings.HASH_FILE, current_hash)
    else:
        print("No changes detected in the data directory. Loading the existing index...")
        index = load_index(settings)

    print(f"Index initialized at startup. Index: {index}")
    app.index = index  

    yield  

app = FastAPI(title="Llama Jhub AI Test", lifespan=lifespan)

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)