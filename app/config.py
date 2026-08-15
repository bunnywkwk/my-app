import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "DevOps FastAPI Service"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", os.getenv("ENV", "development"))
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    # Database configuration
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "myapp_db")
    
    # Direct database URL override (optional)
    DATABASE_URL_OVERRIDE: str = os.getenv("DATABASE_URL", "")

    @property
    def database_url(self) -> str:
        # 1. If explicit DATABASE_URL is provided, use it directly
        if self.DATABASE_URL_OVERRIDE:
            return self.DATABASE_URL_OVERRIDE
        
        # 2. If Postgres credentials are passed, construct PostgreSQL connection string
        if self.POSTGRES_USER and self.POSTGRES_PASSWORD:
            return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        
        # 3. Fallback to local SQLite database for quick local testing without Postgres
        return "sqlite:///./devops_app.db"

settings = Settings()
