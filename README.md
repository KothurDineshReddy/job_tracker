# Job Tracker

A comprehensive full-stack job application tracking system built with FastAPI (backend) and React (frontend).

## 🏗️ Architecture

```
job_tracker/
├── .github/workflows/     # GitHub Actions CI/CD
├── backend/               # FastAPI Backend
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── core/         # Core functionality
│   │   ├── services/     # Business logic
│   │   ├── db/           # Database models
│   │   └── main.py       # FastAPI app
│   ├── tests/            # Backend tests
│   └── requirements.txt  # Python dependencies
├── frontend/             # React Frontend
│   ├── src/              # React source code
│   ├── public/           # Static files
│   └── package.json      # Node.js dependencies
├── infra/docker/         # Docker configurations
├── docker-compose.yml    # Multi-service setup
├── .env.example          # Environment variables template
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Node.js 18+ (for local frontend development)
- Python 3.11+ (for local backend development)

### Using Docker (Recommended)
```bash
# Clone the repository
git clone <your-repo-url>
cd job_tracker

# Copy environment file
cp env.example .env

# Start all services
docker-compose up -d

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Local Development
```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend (in another terminal)
cd frontend
npm install
npm start
```

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Primary database
- **Redis** - Caching and sessions
- **SQLAlchemy** - ORM
- **Alembic** - Database migrations
- **Pydantic** - Data validation

### Frontend
- **React 18** - UI framework
- **Axios** - HTTP client
- **React Router** - Navigation
- **CSS3** - Styling

### DevOps
- **Docker** - Containerization
- **GitHub Actions** - CI/CD pipeline
- **PostgreSQL** - Database
- **Redis** - Caching

## 📋 Features

- ✅ **Job Application Tracking** - Track all your job applications
- ✅ **API Documentation** - Auto-generated with FastAPI
- ✅ **Database Integration** - PostgreSQL with SQLAlchemy
- ✅ **Authentication** - JWT-based auth system
- ✅ **Modern UI** - Responsive React frontend
- ✅ **CI/CD Pipeline** - Automated testing and deployment
- ✅ **Docker Support** - Easy deployment and development

## 🔧 Development

### Backend Development
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend Development
```bash
cd frontend
npm install
npm start
```

### Running Tests
```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

### Code Formatting
```bash
# Backend
cd backend
black .
flake8 .
isort .

# Frontend
cd frontend
npm run format
```

## 🌐 API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/jobs` - Get all jobs (placeholder)
- `GET /docs` - Interactive API documentation

## 🐳 Docker Services

- **postgres** - PostgreSQL database (port 5432)
- **redis** - Redis cache (port 6379)
- **backend** - FastAPI application (port 8000)
- **frontend** - React application (port 3000)

## 🔐 Environment Variables

Copy `env.example` to `.env` and configure:

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/job_tracker
DATABASE_TEST_URL=postgresql://user:password@localhost:5432/job_tracker_test

# API
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True
SECRET_KEY=your-secret-key-here

# Frontend
REACT_APP_API_URL=http://localhost:8000/api
REACT_APP_ENVIRONMENT=development
```

## 📊 CI/CD Pipeline

The project includes GitHub Actions for:
- ✅ Automated testing on multiple Python versions
- ✅ Code linting and formatting checks
- ✅ Build and deployment stages
- ✅ Coverage reporting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions, please open an issue in the GitHub repository.