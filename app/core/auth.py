import jwt
from jwt.exceptions import PyJWTError
from fastapi import HTTPException
from uuid import UUID
from datetime import datetime, timedelta, UTC
from fastapi import status
from ..core.config import settings

ALGORITHM = "HS256"

def create_token(user_id: UUID) -> str:
    """Create JWT token for user."""
    expire = datetime.now(UTC) + timedelta(minutes=settings.access_token_expire_minutes)
    payload = {"sub": str(user_id), "exp": expire}
    return jwt.encode(payload, settings.jwt_secret, algorithm=ALGORITHM)

def verify_token(token: str) -> UUID:
    """Verify JWT token and return user_id."""
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[ALGORITHM])
        return UUID(payload["sub"])
    except PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate token")
