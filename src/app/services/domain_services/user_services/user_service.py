from app.db.user.user_base import UserCreate
from sqlalchemy.orm import Session
from app.db.model_to_db.models import User
from app.db.database_helpers.database import SessionLocal

async def create_user(user: UserCreate):
    db: Session = SessionLocal()
    try:
        new_user = User(
            name=user.name,
            email=user.email,
            password=user.password,
            role_id=user.role_id
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    finally:
        db.close()