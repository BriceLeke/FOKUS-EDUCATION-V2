"""University Model"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.core.database import Base


class University(Base):
    """University information model"""

    __tablename__ = "universities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    country = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    website = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    ranking = Column(Integer, nullable=True)  # Global ranking
    acceptance_rate = Column(String(10), nullable=True)  # e.g., "25%"
    application_fee = Column(String(50), nullable=True)
    tuition_fee = Column(String(50), nullable=True)  # Estimated annual cost
    admission_requirements = Column(Text, nullable=True)
    contact_email = Column(String(255), nullable=True)
    phone = Column(String(20), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    programs = relationship(
        "Program",
        back_populates="university",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<University(id={self.id}, name={self.name}, country={self.country})>"


class Program(Base):
    """University program/degree model"""

    __tablename__ = "programs"

    id = Column(Integer, primary_key=True, index=True)
    university_id = Column(Integer, ForeignKey("universities.id"), nullable=False)
    name = Column(String(255), nullable=False, index=True)
    degree_type = Column(String(50), nullable=False)  # e.g., "Bachelor", "Master"
    field_of_study = Column(String(100), nullable=False)
    duration_years = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)
    entry_requirements = Column(Text, nullable=True)
    course_structure = Column(Text, nullable=True)
    career_outcomes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    university = relationship("University", back_populates="programs")

    def __repr__(self):
        return f"<Program(id={self.id}, name={self.name}, university_id={self.university_id})>"
