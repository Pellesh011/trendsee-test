from uuid import UUID
from typing import Dict, Any
from fastapi import HTTPException
import asyncpg
from ..models.schemas import UserCreate, UserUpdate, UserOut
from ..core.auth import create_token

class UserService:
    @staticmethod
    async def create(conn: asyncpg.Connection, user_data: UserCreate) -> Dict[str, Any]:
        user_id = await conn.fetchval(
            "INSERT INTO users (name) VALUES ($1) RETURNING id",
            user_data.name
        )
        row = await conn.fetchrow("SELECT id, name, created_at, updated_at FROM users WHERE id = $1", user_id)
        return dict(row)

    @staticmethod
    async def get(conn: asyncpg.Connection, user_id: UUID) -> Dict[str, Any]:
        row = await conn.fetchrow(
            "SELECT id, name, created_at, updated_at FROM users WHERE id = $1",
            user_id
        )
        if not row:
            raise HTTPException(404, "User not found")
        return dict(row)

    @staticmethod
    async def update_name(conn: asyncpg.Connection, user_id: UUID, name: str) -> Dict[str, Any]:
        row = await conn.fetchrow(
            "UPDATE users SET name = $1 WHERE id = $2 RETURNING id, name, created_at, updated_at",
            name, user_id
        )
        if not row:
            raise HTTPException(404, "User not found")
        return dict(row)

    @staticmethod
    async def delete(conn: asyncpg.Connection, user_id: UUID) -> bool:
        result = await conn.execute("DELETE FROM users WHERE id = $1", user_id)
        return result == "DELETE 1"

user_service = UserService()
