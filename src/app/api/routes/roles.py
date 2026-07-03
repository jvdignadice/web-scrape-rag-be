from fastapi import APIRouter
from app.db.role.role_base import RoleCreate, RoleResponse
from app.services.domain_services.roles_services.role_service import create_role, get_all_roles
from typing import List

router = APIRouter()

@router.post("/create role", response_model=RoleResponse)
async def create_role_endpoint(role: RoleCreate):   
        new_role = await create_role(role)
        return new_role

@router.get("/get_all_roles", response_model=List[RoleResponse])
async def get_all_roles_endpoint():
    roles = await get_all_roles()
    return roles