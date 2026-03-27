from fastapi import Depends, HTTPException, status, Header, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import AsyncGenerator
from uuid import UUID
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from core.database import get_session
from core.auth import verify_token
from sqlalchemy import select
from models.models import User

security = HTTPBearer()

async def get_db(request: Request) -> AsyncGenerator:
    """Legacy asyncpg pool."""
    if not hasattr(request.app.state, 'db_pool') or request.app.state.db_pool is None:
        raise HTTPException(status_code=500, detail="DB not initialized")
    yield request.app.state.db_pool

async def get_session_dep(request: Request) -> AsyncGenerator[AsyncSession, None]:
    """SQLAlchemy AsyncSession from engine."""
    if not hasattr(request.app.state, 'sa_engine') or request.app.state.sa_engine is None:
        raise HTTPException(status_code=500, detail="SA Engine not initialized")
    engine = request.app.state.sa_engine
    async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)
    session = async_session_maker()
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()

async def get_redis(request: Request) -> AsyncGenerator:
    """Redis client."""
    if not hasattr(request.app.state, 'redis_client') or request.app.state.redis_client is None:
        raise HTTPException(status_code=500, detail="Redis not initialized")
    yield request.app.state.redis_client

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    session: AsyncSession = Depends(get_session_dep)
) -> UUID:
    user_id = verify_token(credentials.credentials)
    # Verify exists
    stmt = select(User.id).where(User.id == user_id)
    result = await session.execute(stmt)
    if not result.scalar():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user")
    return user_id
