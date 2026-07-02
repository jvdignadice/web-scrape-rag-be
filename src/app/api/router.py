from fastapi import APIRouter
from app.api.routes import scrape, rag, users, roles

api_router = APIRouter()

api_router.include_router(scrape.router, prefix="/scrape", tags=["scrape"])
api_router.include_router(rag.router, prefix="/rag", tags=["rag"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(roles.router, prefix="/roles", tags=["roles"])
