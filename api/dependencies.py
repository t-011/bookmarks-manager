from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")

security = HTTPBearer()

async def get_current_user(creds: HTTPAuthorizationCredentials = Depends(security)):
    token = creds.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"], audience="authenticated")
        return payload["sub"]
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
