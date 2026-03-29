# services/cache/redis_post_cache.py

import json
from uuid import UUID
from typing import List, Optional, Dict, Any
from redis.asyncio import Redis


class RedisPostCacheService:
    TTL = 600

    @staticmethod
    async def set_post(redis: Redis, post_id: UUID, data: Dict[str, Any]) -> None:
        await redis.setex(str(post_id), RedisPostCacheService.TTL, json.dumps(data))

    @staticmethod
    async def get_post(redis: Redis, post_id: str) -> Optional[Dict[str, Any]]:
        cached = await redis.get(post_id)
        return json.loads(cached) if cached else None

    @staticmethod
    async def delete_post(redis: Redis, post_id: UUID) -> None:
        await redis.delete(str(post_id))

    @staticmethod
    async def add_user_post(redis: Redis, user_id: UUID, post_id: UUID) -> None:
        await redis.lpush(f"users_posts:{user_id}", str(post_id))

    @staticmethod
    async def get_user_post_ids(redis: Redis, user_id: UUID, skip: int, limit: int) -> List[str]:
        return await redis.lrange(f"users_posts:{user_id}", skip, skip + limit - 1)

    @staticmethod
    async def get_all_user_post_ids(redis: Redis, user_id: UUID) -> List[str]:
        return await redis.lrange(f"users_posts:{user_id}", 0, -1)

    @staticmethod
    async def remove_invalid_posts(redis: Redis, user_id: UUID) -> None:
        key = f"users_posts:{user_id}"
        ids = await redis.lrange(key, 0, -1)

        for pid in ids:
            if not await redis.exists(pid):
                await redis.lrem(key, 1, pid)

    @staticmethod
    async def count_user_posts(redis: Redis, user_id: UUID) -> int:
        return await redis.llen(f"users_posts:{user_id}")