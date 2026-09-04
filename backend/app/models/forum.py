"""Forum Models"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.core.database import Base


class ForumDiscussion(Base):
    """Forum discussion model"""

    __tablename__ = "forum_discussions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text, nullable=False)
    category = Column(String(100), nullable=False)  # e.g., "Career", "University", "Scholarship"
    is_pinned = Column(Boolean, default=False)
    view_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    replies = relationship(
        "ForumReply",
        back_populates="discussion",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<ForumDiscussion(id={self.id}, title={self.title})>"


class ForumReply(Base):
    """Forum reply model"""

    __tablename__ = "forum_replies"

    id = Column(Integer, primary_key=True, index=True)
    discussion_id = Column(
        Integer,
        ForeignKey("forum_discussions.id"),
        nullable=False,
    )
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)
    is_solution = Column(Boolean, default=False)
    upvotes = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    discussion = relationship("ForumDiscussion", back_populates="replies")

    def __repr__(self):
        return f"<ForumReply(id={self.id}, discussion_id={self.discussion_id})>"
