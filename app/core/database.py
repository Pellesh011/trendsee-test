import os
import asyncpg
import fastapi
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession, async_sessionmaker

from .config import settings
from typing import AsyncGenerator


async def init_db_pool() -> asyncpg.Pool:
    """Initialize asyncpg pool (legacy)."""
    dsn = os.getenv("DATABASE_URL") or settings.database_url.format(postgres_password=settings.postgres_password)
    return await asyncpg.create_pool(dsn)

async def init_sa_engine() -> AsyncEngine:
    """Initialize SQLAlchemy async engine."""
    dsn = os.getenv("DATABASE_URL") or settings.database_url.format(postgres_password=settings.postgres_password)
    # Force asyncpg driver for SQLAlchemy asyncio
    engine = create_async_engine(dsn.replace('postgresql://', 'postgresql+asyncpg://'), echo=False)
    return engine

async def get_session(request: fastapi.Request) -> AsyncGenerator[AsyncSession, None]:
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

async def close_db_pool(pool: asyncpg.Pool):
    await pool.close()

async def close_sa_engine(engine: AsyncEngine):
    await engine.dispose()
