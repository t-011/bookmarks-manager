from fastapi import FastAPI
from api.routes import auth, bookmarks

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(bookmarks.router)