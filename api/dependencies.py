from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

security = HTTPBearer()
jwt_secret = os.environ.get("JWT_SECRET")

async def get_current_user(creds: HTTPAuthorizationCredentials = Depends(security)):
    creds.credentials
    try:
        payload = jwt.decode(token, jwt_secret, algorithms=["HS256"])
        return payload["sub"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
