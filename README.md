# FOKUS EDUCATION V2

A modern, AI-powered educational guidance platform empowering students in Cameroon with comprehensive tools for career exploration, university selection, and job placement.

## 🚀 Tech Stack

- **Frontend**: Next.js 14 + TypeScript + Tailwind CSS + React Query
- **Backend**: FastAPI + Python 3.11 + SQLAlchemy ORM
- **Database**: PostgreSQL 15
- **Authentication**: JWT (JSON Web Tokens)
- **AI/ML**: Scikit-learn for career matching
- **Deployment**: Docker + Docker Compose

## 📋 Features

### Current Implementation
- ✅ User Authentication (Signup, Login, JWT)
- ✅ User Profiles with Profile Pictures
- ✅ Career Path Exploration
- ✅ Personalized Career Assessment
- ✅ University Search & Filtering
- ✅ Scholarship Database
- ✅ Internship & Job Listings
- ✅ Resume Builder with PDF Export
- ✅ Peer-to-Peer Forum
- ✅ Resource Library

### Planned Features
- 🔄 AI-Powered Career Recommendations
- 🔄 University Matching Algorithm
- 🔄 Application Tracking System
- 🔄 Real-time Notifications
- 🔄 Interview Preparation Module
- 🔄 Mobile App (React Native)

## 🏗️ Project Structure

```
FOKUS-EDUCATION-V2/
├── backend/              # FastAPI application
│   ├── app/
│   │   ├── main.py      # Application entry point
│   │   ├── models/      # SQLAlchemy models
│   │   ├── schemas/     # Pydantic schemas (request/response)
│   │   ├── crud/        # Database operations
│   │   ├── routes/      # API endpoints
│   │   ├── core/        # Config, security, dependencies
│   │   ├── services/    # Business logic
│   │   └── utils/       # Utility functions
│   ├── tests/           # Unit and integration tests
│   ├── requirements.txt # Python dependencies
│   ├── .env.example     # Environment variables template
│   └── Dockerfile
├── frontend/            # Next.js application
│   ├── app/            # App router pages
│   ├── components/     # Reusable React components
│   ├── services/       # API client services
│   ├── hooks/          # Custom React hooks
│   ├── types/          # TypeScript types
│   ├── styles/         # Global styles
│   ├── public/         # Static assets
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   └── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose
- Git

### Quick Start with Docker

```bash
# Clone the repository
git clone https://github.com/BriceLeke/FOKUS-EDUCATION-V2.git
cd FOKUS-EDUCATION-V2

# Start all services
docker-compose up -d

# Run database migrations (first time only)
docker exec fokus_backend alembic upgrade head

# Create initial seed data (optional)
docker exec fokus_backend python -m app.seed_data
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### Local Development (without Docker)

#### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Run migrations
alembic upgrade head

# Start backend server
uvicorn app.main:app --reload
```

#### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## 📚 API Documentation

Swagger UI documentation available at `http://localhost:8000/docs`

### Key Endpoints

#### Authentication
- `POST /api/auth/signup` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/refresh` - Refresh access token
- `GET /api/auth/me` - Get current user profile

#### Career
- `GET /api/careers` - List all careers
- `GET /api/careers/{id}` - Get career details
- `POST /api/assessments` - Create career assessment
- `GET /api/assessments/{id}` - Get assessment results

#### Universities
- `GET /api/universities` - Search universities
- `GET /api/universities/{id}` - Get university details
- `GET /api/programs` - Search programs

#### Scholarships
- `GET /api/scholarships` - Search scholarships
- `GET /api/scholarships/{id}` - Get scholarship details

#### Jobs & Internships
- `GET /api/internships` - List internships
- `GET /api/jobs` - List jobs
- `POST /api/applications` - Submit application

#### Resume
- `POST /api/resume` - Create/update resume
- `GET /api/resume` - Get user resume
- `POST /api/resume/export-pdf` - Export resume as PDF

#### Forum
- `GET /api/forum/discussions` - List discussions
- `POST /api/forum/discussions` - Create discussion
- `GET /api/forum/discussions/{id}/replies` - Get replies
- `POST /api/forum/discussions/{id}/replies` - Post reply

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## 🔒 Security Features

- ✅ Password hashing with bcrypt
- ✅ JWT authentication with refresh tokens
- ✅ CORS configuration
- ✅ SQL injection prevention (SQLAlchemy ORM)
- ✅ Request validation with Pydantic
- ✅ Rate limiting
- ✅ Secure file uploads with validation
- ✅ Environment-based configuration

## 📈 Performance Optimizations

- Async/await for non-blocking operations
- Database query optimization with eager loading
- Frontend code splitting and lazy loading
- Caching strategies
- CDN-ready static assets

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## 👥 Authors

- **Brice Leke** - Initial concept and implementation

## 📧 Support

For support, email support@fokus-education.com or open an issue on GitHub.

## 🔄 Status

Active Development - V2.0.0-alpha
