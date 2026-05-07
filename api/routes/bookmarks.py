from fastapi import APIRouter, Depends
from api.models import BookmarkCreate, BookmarkOut
from api.database import supabase
from api.dependencies import get_current_user


router = APIRouter()

@router.post("/bookmarks")
async def bookmark_create(data: BookmarkCreate, user_id: str = Depends(get_current_user)):

    res = (
        supabase.table("bookmarks")
        .insert({"user_id": user_id, **data.model_dump()})
        .execute()
    )

    return res.data[0]

@router.get("/bookmarks", response_model=list[BookmarkOut])
async def bookmark_get(user_id: str = Depends(get_current_user)):

    res = (
        supabase.table("bookmarks")
        .select("*").eq("user_id", user_id)
        .execute()
    )

    return res.data