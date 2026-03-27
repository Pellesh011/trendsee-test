from redis.asyncio import Redis
from core.config import settings
from typing import AsyncGenerator

async def init_redis_client() -> Redis:
    return Redis.from_url(
        settings.redis_url.format(redis_password=settings.redis_password),
        decode_responses=True
    )

async def close_redis_client(client: Redis):
    await client.aclose()
