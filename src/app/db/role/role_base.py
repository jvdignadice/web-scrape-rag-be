from pydantic import BaseModel
from typing import Optional
import uuid

class RoleBase(BaseModel):
    name: str
    description: str
    rank: int

class RoleCreate(RoleBase):
    pass

class RoleResponse(RoleBase):
    id: uuid.UUID

    class Config:
        from_attributes = True      
        