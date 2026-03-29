# Trendsee Publications API

Advanced FastAPI service with JWT auth, Redis cache (10min hot posts), Postgres, **Alembic migrations**.

## Quick Start

1. Copy `.env.example` to `.env` and edit values:
```
cp .env.example .env
```

2. Run:
```
docker compose up --build
```

Access:
- Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
