from app.db import db
from datetime import datetime as dt, timezone
from sqlalchemy.orm import Mapped, relationship
from typing import List, TYPE_CHECKING
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import BigInteger, Boolean, Column, DateTime, String


if TYPE_CHECKING:
    from app.api.models.auth import Role, UserRole


class User(db.Model):
    __tablename__ = "users"

    id: Column | int = Column(BigInteger, primary_key=True, nullable=False)
    username: Column | str = Column(String(100), nullable=False, unique=True)
    password: Column | str = Column(String(255), nullable=False)
    admin: Column | bool = Column(Boolean, nullable=False, default=False)
    active: Column | bool = Column(Boolean, nullable=False, default=True)
    created_at: Column | dt = Column(
        DateTime, nullable=False, default=dt.now(timezone.utc)
    )

    token: Column | str = Column(String(255))

    roles: Mapped[List["Role"]] = relationship(
        secondary="users_roles", back_populates="users"
    )

    users_roles: Mapped[List["UserRole"]] = relationship(
        back_populates="user", overlaps="roles,users"
    )

    def __init__(
        self, username: str, password: str, active: bool = True, admin: bool = False
    ) -> None:
        self.username = username
        self.password = generate_password_hash(password)
        self.active = active
        self.admin = admin

    def verify_password_hash(self, password: str) -> bool:
        return check_password_hash(self.password, password)

    def get_user_roles(self):
        roles: list[str] = [role.name for role in self.roles]

        if self.admin is True:
            roles.append("admin")

        return roles
