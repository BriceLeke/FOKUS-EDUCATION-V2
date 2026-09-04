"""Scholarship Model"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, JSON

from app.core.database import Base


class Scholarship(Base):
    """Scholarship opportunities model"""

    __tablename__ = "scholarships"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    provider = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    amount = Column(String(100), nullable=True)  # e.g., "$5,000 - $50,000"
    coverage = Column(String(100), nullable=True)  # e.g., "Full Tuition", "Partial"
    eligibility_criteria = Column(Text, nullable=False)
    required_documents = Column(JSON, nullable=True)  # List of required documents
    application_deadline = Column(DateTime, nullable=False)
    award_date = Column(String(50), nullable=True)  # e.g., "September 2024"
    country = Column(String(100), nullable=True)
    level = Column(String(50), nullable=True)  # e.g., "Bachelor", "Master", "PhD"
    field_of_study = Column(String(100), nullable=True)
    website = Column(String(255), nullable=True)
    contact_email = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Scholarship(id={self.id}, name={self.name})>"
