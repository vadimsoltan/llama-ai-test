from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    REPLICATE_API_TOKEN: str
    DATA_DIRECTORY: str = "./data"
    STORAGE_DIRECTORY: str = "./storage"
    HASH_FILE: str = "./storage/hash.txt"

    class Config:
        env_file = ".env"

def get_settings() -> Settings:
    """Get the settings instance."""
    return Settings()