from uuid import UUID
from typing import Dict, Any
from fastapi import HTTPException
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from models.models import User
from models.schemas import UserCreate, UserOut
from core.auth import create_token

class UserService:
    @staticmethod
    async def create(session: AsyncSession, user_data: UserCreate) -> Dict[str, Any]:
        ins = insert(User).values(name=user_data.name).returning(User.id)
        user_id = await session.scalar(ins)
        stmt = select(User).where(User.id == user_id)
        result = await session.execute(stmt)
        user = result.scalar_one()
        await session.commit()
        return user.__dict__

    @staticmethod
    async def get(session: AsyncSession, user_id: UUID) -> Dict[str, Any]:
        stmt = select(User).where(User.id == user_id)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(404, "User not found")
        return user.__dict__

    @staticmethod
    async def get_by_name(session: AsyncSession, name: str) -> Dict[str, Any]:
        stmt = select(User).where(User.name == name)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(404, "User not found")
        return user.__dict__

    @staticmethod
    async def update_name(session: AsyncSession, user_id: UUID, name: str) -> Dict[str, Any]:
        stmt = update(User).where(User.id == user_id).values(name=name).returning(User)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(404, "User not found")
        await session.commit()
        return user.__dict__

    @staticmethod
    async def delete(session: AsyncSession, user_id: UUID) -> bool:
        stmt = delete(User).where(User.id == user_id)
        result = await session.execute(stmt)
        await session.commit()
        return result.rowcount == 1

user_service = UserService()
