"""SQLAlchemy Models"""
from app.models.user import User
from app.models.career import Career, CareerAssessment
from app.models.university import University, Program
from app.models.scholarship import Scholarship
from app.models.job import Job, Internship, Application
from app.models.resume import Resume
from app.models.forum import ForumDiscussion, ForumReply

__all__ = [
    "User",
    "Career",
    "CareerAssessment",
    "University",
    "Program",
    "Scholarship",
    "Job",
    "Internship",
    "Application",
    "Resume",
    "ForumDiscussion",
    "ForumReply",
]
