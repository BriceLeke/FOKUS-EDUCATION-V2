"""Application Configuration"""
from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # Database
    DATABASE_URL: str = "postgresql://fokus_user:fokus_password@localhost:5432/fokus_education"

    # Security
    SECRET_KEY: str = "your-super-secret-key-change-this-in-production-12345"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    TRUSTED_HOSTS: List[str] = ["localhost", "127.0.0.1"]

    # File Upload
    MAX_UPLOAD_SIZE: int = 5242880  # 5MB
    ALLOWED_UPLOAD_EXTENSIONS: List[str] = [
        "jpg",
        "jpeg",
        "png",
        "pdf",
        "doc",
        "docx",
    ]
    UPLOAD_DIR: str = "uploads"

    # Email (optional)
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""

    # Logging
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
