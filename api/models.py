from pydantic import BaseModel
from datetime import datetime

class UserRegister(BaseModel):
    email: str
    password: str
    name: str

class UserLogin(BaseModel):
    email: str
    password: str

class BookmarkCreate(BaseModel):
    url: str
    note: str | None = None
    tags: list[str] | None = None

class BookmarkOut(BaseModel):
    id: str
    url: str
    note: str | None = None
    tags: list[str] | None = None
    created_at: datetime