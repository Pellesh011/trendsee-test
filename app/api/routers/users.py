from fastapi import APIRouter, Depends
from uuid import UUID
from models.schemas import UserCreate, UserOut, UserUpdate, Token
from api.deps import get_session_dep, get_current_user
from services.users import user_service
from core.auth import create_token
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=Token)
async def create_user(user_data: UserCreate, session: AsyncSession = Depends(get_session_dep)):
    """Create user and return JWT token."""
    user = await user_service.create(session, user_data)
    token = create_token(user["id"])
    return Token(access_token=token)

@router.get("/{user_id}/token", response_model=Token)
async def get_user_token(user_id: UUID, session: AsyncSession = Depends(get_session_dep)):
    """Get JWT token for user by ID (test helper)."""
    await user_service.get(session, user_id)  # Verify
    token = create_token(user_id)
    return Token(access_token=token)

@router.patch("/me/name", response_model=UserOut)
async def update_my_name(
    update_data: UserUpdate,
    user_id: UUID = Depends(get_current_user),
    session: AsyncSession = Depends(get_session_dep)
):
    """Update current user's name."""
    user = await user_service.update_name(session, user_id, update_data.name)
    return UserOut.model_validate(user)

@router.delete("/me", status_code=204)
async def delete_my_account(
    user_id: UUID = Depends(get_current_user),
    session: AsyncSession = Depends(get_session_dep)
):
    """Delete current user account."""
    await user_service.delete(session, user_id)
