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

## Alembic Migrations

Activate venv and run:

```
source venv/bin/activate
alembic upgrade head
```

To generate new migration:
```
alembic revision -m "description"
```

Config uses `.env` postgres_password via `app.core.config.settings`.

**Note:** Run migrations before app startup if changing schema. Can add to docker-compose init.

## Features
- Users: CRUD (JWT on create), /api/v1/users/{id}/token test
- Posts: CRUD (auth req), list /me. Cache Redis 10min, else Postgres +2s sim delay.
- DI: lifespan pools.

## Test (curl, replace TOKEN)

```bash
# Create user + token
TOKEN=$(curl -s -X POST "http://localhost:8000/api/v1/users/" \\
  -H "Content-Type: application/json" \\
  -d '{"name": "Test"}' | jq -r .access_token)

# Get token by id (first need user id from create response)
curl "http://localhost:8000/api/v1/users/USER_ID_HERE/token"

# Create post
curl -s -X POST "http://localhost:8000/api/v1/posts/" \\
  -H "Authorization: Bearer $TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{"title": "Hot Post", "text": "Cached!"}' | jq

# List my posts (fast)
curl -s -H "Authorization: Bearer $TOKEN" http://localhost:8000/api/v1/posts/me | jq

# Update/Delete (auth req)
curl -X PATCH "http://localhost:8000/api/v1/posts/POST_ID" \\
  -H "Authorization: Bearer $TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{"text": "Updated"}'

curl -X DELETE "http://localhost:8000/api/v1/posts/POST_ID" \\
  -H "Authorization: Bearer $TOKEN"

# Wait >10min, get post (should delay 2s)
curl -H "Authorization: Bearer $TOKEN" "http://localhost:8000/api/v1/posts/POST_ID"
```

## Architecture
```
app/
├── core/ (config, db/redis pools, auth)
├── models/ (schemas.py, models.py SQLAlchemy)
├── api/ (deps, routers)
├── services/ (business)
└── main.py

alembic/ (migrations)
venv/ (python deps)
```

## Local Dev (no Docker)
```
pip install -r app/requirements.txt  # or use venv
uvicorn app.main:app --reload
```

DB: postgres://postgres@${POSTGRES_PASSWORD}@localhost:5432/trendsee
Redis: localhost:6379

Run `alembic upgrade head` before app.

Enjoy!
