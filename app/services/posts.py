from uuid import UUID
from typing import Dict, Any, List, Optional
from fastapi import HTTPException
import asyncio
import json
import asyncpg
from sqlalchemy import select, desc, text
from ..models.models import Post
from redis.asyncio import Redis
from ..models.schemas import PostCreate, PostUpdate, PostOut
from ..services.users import user_service  # Not direct, but for ownership check
from sqlalchemy import select, desc, text
from ..models.models import Post

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
        await redis.lpush(f"users_posts:{user_id}", str(post_id))
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
    async def get_user_posts(
        redis: Redis, 
        conn: asyncpg.Connection, 
        user_id: UUID, 
        skip: int = 0, 
        limit: int = 10
    ) -> Dict[str, Any]:
        key = f"users_posts:{user_id}"
        
        # Clean invalid posts from Redis list
        all_post_ids_str = await redis.lrange(key, 0, -1)
        invalid_ids = []
        for post_id_str in all_post_ids_str:
            if not await redis.exists(post_id_str):
                invalid_ids.append(post_id_str)
        for inv_id in invalid_ids:
            await redis.lrem(key, 1, inv_id)
        
        # Get total from Redis list
        total = await redis.llen(key)
        
        # Fetch Redis posts for this page
        end_idx = skip + limit
        redis_post_ids_str = await redis.lrange(key, skip, end_idx - 1)
        redis_posts = []
        redis_ids = set()
        for post_id_str in redis_post_ids_str:
            cached = await redis.get(post_id_str)
            if cached:
                post_dict = json.loads(cached)
                redis_posts.append(post_dict)
                redis_ids.add(post_id_str)
        
        # Compute gap
        gap = limit - len(redis_posts)
        db_posts = []
        
        if gap > 0:
            # Fetch old posts from DB to fill gap (newest first among old)
            stmt = select(Post).where(
                Post.user_id == user_id,
                Post.created_at < text("NOW() - INTERVAL '10 minutes'")
            ).order_by(desc(Post.created_at)).limit(gap)
            result = await conn.execute(stmt)
            rows = result.fetchall()
            
            for row in rows:
                post_dict = dict(row._mapping)
                post_id_str = str(post_dict['id'])
                if post_id_str not in redis_ids:
                    # Cache it
                    await redis.setex(post_id_str, 600, json.dumps(post_dict))
                    # Add to list if needed (LPUSH to Redis list?)
                    await redis.lpush(key, post_id_str)
                    db_posts.append(post_dict)
                    redis_ids.add(post_id_str)  # Update to avoid dup
        
        # Merge and sort DESC by created_at
        all_posts = redis_posts + db_posts
        all_posts.sort(key=lambda p: p['created_at'], reverse=True)
        
        # Slice to exact page
        items = all_posts[:limit]
        
        return {
            "items": items,
            "total": total + len(db_posts),  # Approximate total including newly added
            "skip": skip,
            "limit": limit
        }


post_service = PostService()
