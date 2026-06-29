from fastapi import APIRouter
from app.api.routes import scrape, rag

api_router = APIRouter()

api_router.include_router(scrape.router, prefix="/scrape", tags=["scrape"])
api_router.include_router(rag.router, prefix="/rag", tags=["rag"])