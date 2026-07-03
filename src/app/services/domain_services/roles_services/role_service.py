from app.db.role.role_base import RoleCreate, RoleResponse
from app.db.model_to_db.models import Role
from sqlalchemy.orm import Session
from app.db.database_helpers.database import SessionLocal


async def create_role(role: RoleCreate):
    db: Session = SessionLocal()
    try:
        new_role = Role(
            name=role.name,
            description=role.description,
            rank=role.rank
        )
        db.add(new_role)
        db.commit()
        db.refresh(new_role)
        return new_role
    finally:
        db.close()

async def get_all_roles():
    db: Session = SessionLocal()
    try:
        roles = db.query(Role).all()
        return roles
    finally:
        db.close() 