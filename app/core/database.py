import os
import asyncpg
from ..core.config import settings
from typing import AsyncGenerator

async def init_db_pool() -> asyncpg.Pool:
    dsn = os.getenv("DATABASE_URL") or settings.database_url.format(postgres_password=settings.postgres_password)
    return await asyncpg.create_pool(dsn)

async def close_db_pool(pool: asyncpg.Pool):
    await pool.close()
