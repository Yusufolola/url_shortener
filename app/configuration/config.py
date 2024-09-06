from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./url.db"
    PORT: int = 8000

settings = Settings()

