import os
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.replicate import Replicate
from transformers import AutoTokenizer
from app.models.settings import Settings as AppSettings

def configure_llama_index(settings: AppSettings):
    """Configure Llama Index with the provided settings."""
    print("Starting Llama Index configuration...")
    llama2_7b_chat = "meta/meta-llama-3-8b-instruct"
    try:
        print("Configuring Replicate LLM...")
        # Set the environment variable dynamically
        os.environ["REPLICATE_API_TOKEN"] = settings.REPLICATE_API_TOKEN
        print(f"Using Replicate API token: {settings.REPLICATE_API_TOKEN}")
        Settings.llm = Replicate(
            model=llama2_7b_chat,
            temperature=0.01,
            additional_kwargs={"top_p": 1, "max_new_tokens": 300},
        )
        print("Replicate LLM configured successfully.")
    except Exception as e:
        print(f"Error configuring Replicate LLM: {e}")
        raise

    try:
        print("Configuring tokenizer...")
        Settings.tokenizer = AutoTokenizer.from_pretrained("NousResearch/Llama-2-7b-chat-hf")
        print("Tokenizer configured successfully.")
    except Exception as e:
        print(f"Error configuring tokenizer: {e}")
        raise

    try:
        print("Configuring embedding model...")
        Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        print("Embedding model configured successfully.")
    except Exception as e:
        print(f"Error configuring embedding model: {e}")
        raise

def create_index(settings: AppSettings):
    """Create a new index from documents in the data directory."""
    configure_llama_index(settings)
    try:
        documents = SimpleDirectoryReader(settings.DATA_DIRECTORY).load_data()
        if not documents:
            print("No documents found in the data directory. Creating an empty index.")
            index = VectorStoreIndex([])
        else:
            index = VectorStoreIndex.from_documents(documents)
    except (FileNotFoundError, ValueError) as e:
        # Handle missing or empty data directory
        print(f"Error loading documents: {e}. Creating an empty index.")
        index = VectorStoreIndex([])

    index.storage_context.persist(persist_dir=settings.STORAGE_DIRECTORY)
    return index

def load_index(settings: AppSettings):
    """Load an existing index from the storage directory."""
    configure_llama_index(settings)
    storage_context = StorageContext.from_defaults(persist_dir=settings.STORAGE_DIRECTORY)
    return load_index_from_storage(storage_context)