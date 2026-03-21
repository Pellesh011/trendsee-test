from fastapi import Depends, HTTPException, status, Header, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Generator
from uuid import UUID
from ..core.auth import verify_token
import asyncpg
from redis.asyncio import Redis
from ..models.schemas import UserOut  # Forward

security = HTTPBearer()

async def get_db(request: Request) -> Generator[asyncpg.Pool, None, None]:
    if not hasattr(request.app.state, 'db_pool') or request.app.state.db_pool is None:
        raise HTTPException(status_code=500, detail="DB not initialized")
    yield request.app.state.db_pool

async def get_redis(request: Request) -> Generator[Redis, None, None]:
    if not hasattr(request.app.state, 'redis_client') or request.app.state.redis_client is None:
        raise HTTPException(status_code=500, detail="Redis not initialized")
    yield request.app.state.redis_client

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: asyncpg.Pool = Depends(get_db)
) -> UUID:
    user_id = verify_token(credentials.credentials)
    # Verify exists
    async with db.acquire() as conn:
        row = await conn.fetchrow("SELECT id FROM users WHERE id = $1", user_id)
        if not row:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user")
    return user_id
