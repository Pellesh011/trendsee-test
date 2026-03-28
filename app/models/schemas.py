from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID
from datetime import datetime
from pydantic import ConfigDict

class UserCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str = Field(..., min_length=1, max_length=255)

class UserUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: Optional[str] = Field(None, min_length=1, max_length=255)

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime

class PostCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str = Field(..., min_length=1, max_length=255)
    text: str = Field(..., min_length=1)

class PostUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    text: Optional[str] = Field(None, min_length=1)

class PostOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    user_id: UUID
    title: str
    text: str
    created_at: datetime
    updated_at: datetime

class Pagination(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    items: List[PostOut] = Field(default_factory=list)
    total: int
    skip: int
    limit: int

class UserLogin(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str = Field(..., min_length=1, max_length=255)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
