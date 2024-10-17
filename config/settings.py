from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    gemini_api_key: str
    mongo_db_url: str
    redis_host: str
    redis_port: int

    class Config:
        env_file = ".env"

settings = Settings()
