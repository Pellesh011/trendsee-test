from fastapi import APIRouter, Depends
from uuid import UUID
from ...models.schemas import UserCreate, UserOut, UserUpdate, Token
from ...api.deps import get_db, get_current_user
from ...services.users import user_service
from ...core.auth import create_token
import asyncpg

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=Token)
async def create_user(user_data: UserCreate, db: asyncpg.Pool = Depends(get_db)):
    """Create user and return JWT token."""
    async with db.acquire() as conn:
        user = await user_service.create(conn, user_data)
    token = create_token(user["id"])
    return Token(access_token=token)

@router.get("/{user_id}/token", response_model=Token)
async def get_user_token(user_id: UUID, db: asyncpg.Pool = Depends(get_db)):
    """Get JWT token for user by ID (test helper)."""
    async with db.acquire() as conn:
        await user_service.get(conn, user_id)  # Verify
    token = create_token(user_id)
    return Token(access_token=token)

@router.patch("/me/name", response_model=UserOut)
async def update_my_name(
    update_data: UserUpdate,
    user_id: UUID = Depends(get_current_user),
    db: asyncpg.Pool = Depends(get_db)
):
    """Update current user's name."""
    async with db.acquire() as conn:
        user = await user_service.update_name(conn, user_id, update_data.name)
    return UserOut.model_validate(user)

@router.delete("/me", status_code=204)
async def delete_my_account(
    user_id: UUID = Depends(get_current_user),
    db: asyncpg.Pool = Depends(get_db)
):
    """Delete current user account."""
    async with db.acquire() as conn:
        await user_service.delete(conn, user_id)
