"""Main FastAPI Application"""
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.core.config import settings
from app.core.database import engine, Base
from app.routes import auth, users, careers, universities, scholarships, jobs, resume, forum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle management"""
    # Startup
    logger.info("Starting FOKUS EDUCATION Backend")
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown
    logger.info("Shutting down FOKUS EDUCATION Backend")


app = FastAPI(
    title="FOKUS EDUCATION API",
    description="AI-Powered Educational Guidance Platform",
    version="2.0.0-alpha",
    lifespan=lifespan,
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.TRUSTED_HOSTS,
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to FOKUS EDUCATION API",
        "version": "2.0.0-alpha",
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(careers.router, prefix="/api/careers", tags=["Careers"])
app.include_router(universities.router, prefix="/api/universities", tags=["Universities"])
app.include_router(scholarships.router, prefix="/api/scholarships", tags=["Scholarships"])
app.include_router(jobs.router, prefix="/api/jobs", tags=["Jobs & Internships"])
app.include_router(resume.router, prefix="/api/resume", tags=["Resume"])
app.include_router(forum.router, prefix="/api/forum", tags=["Forum"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
