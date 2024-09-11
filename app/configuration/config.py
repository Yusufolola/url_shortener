from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = postgresql://url_user:qBvV7npSVZnZvSrMjmbz2BOcv3T1H5LE@dpg-crgj6jjv2p9s73achkt0-a/url_v7th
    PORT: int = 8000

settings = Settings()

