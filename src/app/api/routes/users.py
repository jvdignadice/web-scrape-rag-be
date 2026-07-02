from fastapi import APIRouter
from app.db.user.user_base import UserCreate, UserResponse
from app.services.domain_services.user_services.user_service import create_user

router = APIRouter()

@router.post("/create_user", response_model=UserResponse)
async def create_user_endpoint(user: UserCreate):
    new_user = await create_user(user)
    return new_user