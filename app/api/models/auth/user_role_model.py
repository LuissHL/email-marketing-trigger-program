from app.db import db
from typing import TYPE_CHECKING
from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.orm import Mapped, relationship


if TYPE_CHECKING:
    from app.api.models.auth import User, Role


class UserRole(db.Model):
    __tablename__ = "users_roles"

    id: Column | int = Column(BigInteger, primary_key=True, nullable=False)

    user_id: int = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(
        "User", back_populates="users_roles", overlaps="roles,users"
    )

    role_id: int = Column(BigInteger, ForeignKey("roles.id"), nullable=False)
    role: Mapped["Role"] = relationship(
        "Role", back_populates="users_roles", overlaps="roles,users"
    )
