from fastapi import APIRouter
from api.models import UserLogin, UserRegister
from api.database import supabase

router = APIRouter()

@router.post("/register")
async def register(user: UserRegister):
    res = supabase.auth.sign_up({
        "email": user.email,
        "password": user.password
    })

    return res.user

@router.post("/login")
async def login(user: UserLogin):
    res = supabase.auth.sign_in_with_password({
        "email": user.email,
        "password": user.password
    })
    return res.session
