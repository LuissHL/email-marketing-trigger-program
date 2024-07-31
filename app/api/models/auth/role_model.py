from app.db import db
from typing import List, TYPE_CHECKING
from sqlalchemy import BigInteger, Column, String
from sqlalchemy.orm import Mapped, relationship


if TYPE_CHECKING:
    from app.api.models.auth import User, UserRole


class Role(db.Model):
    __tablename__ = "roles"

    id: Column | int = Column(BigInteger, primary_key=True, nullable=False)
    name: Column | str = Column(String(100), nullable=False, unique=True)
    description: Column | str = Column(String(100))

    users: Mapped[List["User"]] = relationship(
        secondary="users_roles", back_populates="roles"
    )
    users_roles: Mapped[List["UserRole"]] = relationship(
        back_populates="role", overlaps="roles,users"
    )
