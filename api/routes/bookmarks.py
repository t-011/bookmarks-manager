from fastapi import APIRouter, Depends
from models import BookmarkCreate, BookmarkOut
from database import supabase
from dependencies import get_current_user


router = APIRouter()

@router.post("/bookmarks")
async def bookmark_create(data: BookmarkCreate, user_id: str = Depends(get_current_user)):

    res = (
        supabase.table("bookmarks")
        .insert({"user_id": user_id, **data.model_dump()})
        .execute()
    )

    return res.data

@router.get("/bookmarks", response_model=BookmarkOut)
async def bookmark_get(user_id: str = Depends(get_current_user)):

    res = (
        supabase.table("bookmarks")
        .select("*").eq("user_id", user_id)
        .execute()
    )

    return res.data