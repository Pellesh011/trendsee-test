from uuid import UUID
from typing import Dict, Any, List, Optional
from fastapi import HTTPException
import asyncio
import json
from sqlalchemy import select, insert, update, delete, and_, desc, text
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Post
from redis.asyncio import Redis
from models.schemas import PostCreate, PostUpdate, PostOut

class PostService:
    @staticmethod
    async def create(
        session: AsyncSession,
        redis: Redis,
        user_id: UUID,
        post_data: PostCreate
    ) -> Dict[str, Any]:
        try:
            ins = insert(Post).values(
                user_id=user_id, 
                title=post_data.title, 
                text=post_data.text
            ).returning(Post.id)
            post_id = await session.scalar(ins)
            stmt = select(Post).where(Post.id == post_id)
            result = await session.execute(stmt)
            post = result.scalar_one()
            await session.commit()
            post_obj = PostOut.model_validate(post)
            post_dict = post_obj.model_dump(mode='json')
            await redis.setex(str(post_id), 600, json.dumps(post_dict))
            await redis.lpush(f"users_posts:{user_id}", str(post_id))
            return post_dict
        except Exception as e:
            print(e) 
            return {}

    @staticmethod
    async def update(
        session: AsyncSession,
        redis: Redis,
        post_id: UUID,
        user_id: UUID,
        title: Optional[str] = None,
        text: Optional[str] = None
    ) -> Dict[str, Any]:
        if title is None and text is None:
            raise HTTPException(400, "At least one field required")
        values = {}
        if title is not None:
            values['title'] = title
        if text is not None:
            values['text'] = text
        values['updated_at'] = text('CURRENT_TIMESTAMP')
        stmt = update(Post).where(and_(Post.id == post_id, Post.user_id == user_id)).values(**values).returning(Post)
        result = await session.execute(stmt)
        post = result.scalar_one_or_none()
        if not post:
            raise HTTPException(404, "Post not found or unauthorized")
        await session.commit()
        post_obj = PostOut.model_validate(post)
        post_dict = post_obj.model_dump(mode='json')
        await redis.setex(str(post_id), 600, json.dumps(post_dict))
        return post_dict

    @staticmethod
    async def delete(
        session: AsyncSession,
        redis: Redis,
        post_id: UUID,
        user_id: UUID
    ) -> bool:
        stmt = delete(Post).where(and_(Post.id == post_id, Post.user_id == user_id))
        result = await session.execute(stmt)
        await session.commit()
        if result.rowcount == 1:
            await redis.delete(str(post_id))
            return True
        return False

    @staticmethod
    async def get_user_posts(
        redis: Redis, 
        session: AsyncSession, 
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
                post_dict_raw = json.loads(cached)
                post_obj = PostOut.model_validate(post_dict_raw)
                post_dict = post_obj.model_dump(mode='json')
                redis_posts.append(post_dict)
                redis_ids.add(post_id_str)
        
        # Compute gap
        gap = limit - len(redis_posts)
        db_posts = []
        
        if gap > 0:
            # Fetch old posts from DB to fill gap (newest first among old)
            stmt = select(Post).where(
                and_(
                    Post.user_id == user_id,
                    Post.created_at < text("NOW() - INTERVAL '10 minutes'")
                )
            ).order_by(desc(Post.created_at)).limit(gap)
            result = await session.execute(stmt)
            rows = result.fetchall()
            
            for row in rows:
                post = row.Post
                post_obj = PostOut.model_validate(post)
                post_dict = post_obj.model_dump(mode='json')
                post_id_str = str(post_dict['id'])
                if post_id_str not in redis_ids:
                    db_posts.append(post_dict)
        
        # Merge and sort DESC by created_at
        all_posts = redis_posts + db_posts
        all_posts.sort(key=lambda p: p['created_at'], reverse=True)
        
        # Slice to exact page
        items = all_posts[:limit]
        
        return {
            "items": items,
            "total": total + len(db_posts),
            "skip": skip,
            "limit": limit
        }

post_service = PostService()
