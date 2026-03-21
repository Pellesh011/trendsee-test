from uuid import UUID
from typing import Dict, Any, List, Optional
from fastapi import HTTPException
import asyncio
import json
import asyncpg
from redis.asyncio import Redis
from ..models.schemas import PostCreate, PostUpdate, PostOut
from ..services.users import user_service  # Not direct, but for ownership check

class PostService:
    @staticmethod
    async def create(
        conn: asyncpg.Connection,
        redis: Redis,
        user_id: UUID,
        post_data: PostCreate
    ) -> Dict[str, Any]:
        post_id = await conn.fetchval(
            "INSERT INTO posts (user_id, title, text) VALUES ($1, $2, $3) RETURNING id",
            user_id, post_data.title, post_data.text
        )
        row = await conn.fetchrow(
            "SELECT * FROM posts WHERE id = $1",
            post_id
        )
        post_dict = dict(row)
        await redis.setex(str(post_id), 600, json.dumps(post_dict))
        return post_dict

    @staticmethod
    async def get(
        redis: Redis,
        conn: asyncpg.Connection,
        post_id: UUID,
        user_id: UUID
    ) -> Dict[str, Any]:
        post_str_id = str(post_id)
        cached = await redis.get(post_str_id)
        if cached:
            return json.loads(cached)
        row = await conn.fetchrow("SELECT * FROM posts WHERE id = $1 AND user_id = $2", post_id, user_id)
        if not row:
            raise HTTPException(404, "Post not found or unauthorized")
        post_dict = dict(row)
        await redis.setex(post_str_id, 600, json.dumps(post_dict))
        await asyncio.sleep(2)
        return post_dict

    @staticmethod
    async def update(
        conn: asyncpg.Connection,
        redis: Redis,
        post_id: UUID,
        user_id: UUID,
        title: Optional[str],
        text: Optional[str]
    ) -> Dict[str, Any]:
        if not title and not text:
            raise HTTPException(400, "At least one field required")
        updates = []
        params = []
        i = 1
        if title:
            updates.append(f"title = ${i}")
            params.append(title)
            i += 1
        if text:
            updates.append(f"text = ${i}")
            params.append(text)
            i += 1
        params.append(post_id)
        params.append(user_id)
        query = f"UPDATE posts SET {', '.join(updates)}, updated_at = CURRENT_TIMESTAMP WHERE id = ${i} AND user_id = ${i+1} RETURNING *"
        row = await conn.fetchrow(query, *params)
        if not row:
            raise HTTPException(404, "Post not found or unauthorized")
        post_dict = dict(row)
        await redis.setex(str(post_id), 600, json.dumps(post_dict))
        return post_dict

    @staticmethod
    async def delete(
        conn: asyncpg.Connection,
        redis: Redis,
        post_id: UUID,
        user_id: UUID
    ) -> bool:
        result = await conn.execute(
            "DELETE FROM posts WHERE id = $1 AND user_id = $2",
            post_id, user_id
        )
        if result == "DELETE 1":
            await redis.delete(str(post_id))
            return True
        return False

    @staticmethod
    async def get_user_posts(conn: asyncpg.Connection, user_id: UUID) -> List[Dict[str, Any]]:
        rows = await conn.fetch(
            "SELECT * FROM posts WHERE user_id = $1 ORDER BY created_at DESC",
            user_id
        )
        return [dict(row) for row in rows]

post_service = PostService()
