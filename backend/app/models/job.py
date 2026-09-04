"""Job and Internship Models"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship

from app.core.database import Base


class Job(Base):
    """Job posting model"""

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    company = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    job_type = Column(String(50), nullable=False)  # e.g., "Full-time", "Part-time"
    description = Column(Text, nullable=False)
    requirements = Column(Text, nullable=False)
    salary_range = Column(String(100), nullable=True)
    benefits = Column(Text, nullable=True)
    application_link = Column(String(500), nullable=True)
    posting_date = Column(DateTime, default=datetime.utcnow)
    deadline = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    applications = relationship(
        "Application",
        back_populates="job",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Job(id={self.id}, title={self.title}, company={self.company})>"


class Internship(Base):
    """Internship opportunity model"""

    __tablename__ = "internships"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    company = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    duration = Column(String(100), nullable=True)  # e.g., "3 months", "6 months"
    description = Column(Text, nullable=False)
    requirements = Column(Text, nullable=False)
    stipend = Column(String(100), nullable=True)
    benefits = Column(Text, nullable=True)
    application_link = Column(String(500), nullable=True)
    posting_date = Column(DateTime, default=datetime.utcnow)
    deadline = Column(DateTime, nullable=True)
    start_date = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    applications = relationship(
        "Application",
        back_populates="internship",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Internship(id={self.id}, title={self.title}, company={self.company})>"


class Application(Base):
    """Job/Internship application model"""

    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=True)
    internship_id = Column(Integer, ForeignKey("internships.id"), nullable=True)
    status = Column(
        String(50),
        default="pending",
        nullable=False,
    )  # pending, accepted, rejected, withdrawn
    cover_letter = Column(Text, nullable=True)
    resume_id = Column(Integer, ForeignKey("resumes.id"), nullable=True)
    applied_date = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    job = relationship("Job", back_populates="applications")
    internship = relationship("Internship", back_populates="applications")

    def __repr__(self):
        return f"<Application(id={self.id}, user_id={self.user_id}, status={self.status})>"
