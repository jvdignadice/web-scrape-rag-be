from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database_helpers.database import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    role_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("roles.id"))

class Role(Base):
    __tablename__ = "roles"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4, server_default=text("gen_random_uuid()"))
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    rank: Mapped[int]

    