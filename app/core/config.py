from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    postgres_password: str
    redis_password: str
    jwt_secret: str
    database_url: Optional[str] = "postgresql://postgres:{postgres_password}@postgres:5432/trendsee"
    redis_url: Optional[str] = "redis://default:{redis_password}@redis:6379/0"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
