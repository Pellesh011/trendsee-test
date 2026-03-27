from fastapi import APIRouter, Depends, status, Query
from uuid import UUID
from typing import List
from models.schemas import PostCreate, PostOut, PostUpdate, Pagination
from api.deps import get_session_dep, get_redis, get_current_user
from services.posts import post_service
from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=PostOut, status_code=status.HTTP_201_CREATED)
async def create_post(
    post_data: PostCreate,
    user_id: UUID = Depends(get_current_user),
    session: AsyncSession = Depends(get_session_dep),
    redis: Redis = Depends(get_redis)
):
    """Create new publication (cached in Redis 10min)."""
    post = await post_service.create(session, redis, user_id, post_data)
    print(post)
    return PostOut.model_validate(post)

@router.get("/me", response_model=Pagination)
async def list_my_posts(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    user_id: UUID = Depends(get_current_user),
    redis: Redis = Depends(get_redis),
    session: AsyncSession = Depends(get_session_dep)
):
    """Get paginated publications of current user (Redis-optimized). Query params: skip, limit."""
    result = await post_service.get_user_posts(redis, session, user_id, skip, limit)
    return Pagination.model_validate(result)

@router.patch("/{post_id}", response_model=PostOut)
async def update_post(
    post_id: UUID,
    update_data: PostUpdate,
    user_id: UUID = Depends(get_current_user),
    session: AsyncSession = Depends(get_session_dep),
    redis: Redis = Depends(get_redis)
):
    """Update publication (owner only, refresh cache)."""
    post = await post_service.update(session, redis, post_id, user_id, update_data.title, update_data.text)
    return PostOut.model_validate(post)

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post_id: UUID,
    user_id: UUID = Depends(get_current_user),
    session: AsyncSession = Depends(get_session_dep),
    redis: Redis = Depends(get_redis)
):
    """Delete publication (owner only, invalidate cache)."""
    success = await post_service.delete(session, redis, post_id, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
