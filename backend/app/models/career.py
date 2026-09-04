"""Career Model"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.core.database import Base


class Career(Base):
    """Career information model"""

    __tablename__ = "careers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    description = Column(Text, nullable=False)
    requirements = Column(Text, nullable=True)
    salary_range = Column(String(100), nullable=True)
    growth_rate = Column(String(50), nullable=True)
    industry = Column(String(100), nullable=True)
    related_fields = Column(JSON, nullable=True)  # List of related careers
    skills_required = Column(JSON, nullable=True)  # List of required skills
    educational_path = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    assessments = relationship(
        "CareerAssessment",
        back_populates="career",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Career(id={self.id}, title={self.title})>"


class CareerAssessment(Base):
    """Career assessment results"""

    __tablename__ = "career_assessments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    career_id = Column(Integer, ForeignKey("careers.id"), nullable=False)
    score = Column(Integer, nullable=False)  # Percentage match (0-100)
    answers = Column(JSON, nullable=True)  # Store assessment answers
    recommendations = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    career = relationship("Career", back_populates="assessments")

    def __repr__(self):
        return f"<CareerAssessment(user_id={self.user_id}, career_id={self.career_id}, score={self.score})>"
