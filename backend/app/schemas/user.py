"""User Schemas"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Base user schema"""

    email: EmailStr
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    phone: Optional[str] = None
    bio: Optional[str] = None


class UserCreate(UserBase):
    """User creation schema"""

    password: str = Field(..., min_length=8, max_length=255)


class UserUpdate(BaseModel):
    """User update schema"""

    first_name: Optional[str] = Field(None, min_length=1, max_length=100)
    last_name: Optional[str] = Field(None, min_length=1, max_length=100)
    phone: Optional[str] = None
    bio: Optional[str] = None


class UserResponse(UserBase):
    """User response schema"""

    id: int
    profile_picture: Optional[str] = None
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserProfileResponse(UserResponse):
    """Detailed user profile response"""

    pass
