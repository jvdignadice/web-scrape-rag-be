from fastapi import APIRouter
from app.db.user.user_base import UserCreate, UserResponse
from app.services.domain_services.user_services.user_service import create_user, get_user_by_id
import uuid

router = APIRouter()

@router.post("/create_user", response_model=UserResponse)
async def create_user_endpoint(user: UserCreate):
    new_user = await create_user(user)
    return new_user

@router.get("/get_user_by_id/{user_id}", response_model=UserResponse)
async def get_user_by_id_endpoint(user_id: uuid.UUID):
    # Implementation for fetching user by ID
    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user