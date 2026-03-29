# services/posts.py

from uuid import UUID
from typing import Dict, Any, Optional, List
from fastapi import HTTPException
from sqlalchemy import select, insert, update, delete, and_, desc, text, func
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Post
from models.schemas import PostCreate, PostOut
from redis.asyncio import Redis

from .redis_post_cache import RedisPostCacheService as cache


class PostService:
    @staticmethod
    async def create(session: AsyncSession, redis: Redis, user_id: UUID, post_data: PostCreate) -> Dict[str, Any]:
        ins = insert(Post).values(
            user_id=user_id,
            title=post_data.title,
            text=post_data.text
        ).returning(Post.id)

        post_id = await session.scalar(ins)

        result = await session.execute(select(Post).where(Post.id == post_id))
        post = result.scalar_one()

        await session.commit()

        post_dict = PostOut.model_validate(post).model_dump(mode='json')

        await cache.set_post(redis, post_id, post_dict)
        await cache.add_user_post(redis, user_id, post_id)

        return post_dict

    @staticmethod
    async def update(
        session: AsyncSession,
        redis: Redis,
        post_id: UUID,
        user_id: UUID,
        title: Optional[str],
        text: Optional[str]
    ) -> Dict[str, Any]:

        if not title and not text:
            raise HTTPException(400, "At least one field required")

        values = {}
        if title:
            values["title"] = title
        if text:
            values["text"] = text

        stmt = (
            update(Post)
            .where(and_(Post.id == post_id, Post.user_id == user_id))
            .values(**values)
            .returning(Post)
        )

        result = await session.execute(stmt)
        post = result.scalar_one_or_none()

        if not post:
            raise HTTPException(404, "Post not found or unauthorized")

        await session.commit()

        post_dict = PostOut.model_validate(post).model_dump(mode='json')

        await cache.set_post(redis, post_id, post_dict)

        return post_dict

    @staticmethod
    async def delete(session: AsyncSession, redis: Redis, post_id: UUID, user_id: UUID) -> bool:
        stmt = delete(Post).where(and_(Post.id == post_id, Post.user_id == user_id))

        result = await session.execute(stmt)
        await session.commit()

        if result.rowcount == 1:
            await cache.delete_post(redis, post_id)
            return True

        return False

    @staticmethod
    async def get_user_posts(
        redis: Redis,
        session: AsyncSession,
        user_id: UUID,
        skip: int,
        limit: int
    ) -> Dict[str, Any]:

        await cache.remove_invalid_posts(redis, user_id)

        total = await cache.count_user_posts(redis, user_id)

        ids = await cache.get_user_post_ids(redis, user_id, skip, limit)

        redis_posts = []
        redis_ids = set()

        for pid in ids:
            data = await cache.get_post(redis, pid)
            if data:
                redis_posts.append(data)
                redis_ids.add(pid)

        gap = limit - len(redis_posts)
        db_posts = []

        if gap > 0:
            stmt = (
                select(Post)
                .where(
                    and_(
                        Post.user_id == user_id,
                        Post.created_at < (func.now() - text("INTERVAL '10 minutes'"))
                    )
                )
                .order_by(desc(Post.created_at))
                .limit(gap)
            )

            result = await session.execute(stmt)

            for row in result.fetchall():
                post = row.Post
                post_dict = PostOut.model_validate(post).model_dump(mode='json')

                if str(post_dict["id"]) not in redis_ids:
                    db_posts.append(post_dict)

        all_posts = redis_posts + db_posts
        all_posts.sort(key=lambda x: x["created_at"], reverse=True)

        return {
            "items": all_posts[:limit],
            "total": total + len(db_posts),
            "skip": skip,
            "limit": limit
        }


post_service = PostService()