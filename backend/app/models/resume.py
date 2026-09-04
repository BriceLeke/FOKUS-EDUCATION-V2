"""Resume Model"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON

from app.core.database import Base


class Resume(Base):
    """User resume model"""

    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    profile_summary = Column(Text, nullable=True)
    education = Column(JSON, nullable=True)  # List of education records
    experience = Column(JSON, nullable=True)  # List of work experiences
    skills = Column(JSON, nullable=True)  # List of skills
    projects = Column(JSON, nullable=True)  # List of projects
    certifications = Column(JSON, nullable=True)  # List of certifications
    languages = Column(JSON, nullable=True)  # List of languages
    references = Column(JSON, nullable=True)  # List of references
    profile_photo = Column(String(255), nullable=True)
    is_active = Column(String(50), default="active")  # active, inactive
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Resume(id={self.id}, user_id={self.user_id}, title={self.title})>"
