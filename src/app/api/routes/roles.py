from fastapi import APIRouter
from app.db.role.role_base import RoleCreate, RoleResponse
from app.services.domain_services.roles_services.role_service import create_role
router = APIRouter()

@router.post("/create role", response_model=RoleResponse)
async def create_role_endpoint(role: RoleCreate):   
        new_role = await create_role(role)
        return new_role