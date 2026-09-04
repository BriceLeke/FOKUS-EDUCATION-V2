"""Authentication Schemas"""
from pydantic import BaseModel, EmailStr


class SignupRequest(BaseModel):
    """User signup request"""

    email: EmailStr
    password: str
    first_name: str
    last_name: str


class LoginRequest(BaseModel):
    """User login request"""

    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """Token response"""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshTokenRequest(BaseModel):
    """Refresh token request"""

    refresh_token: str
