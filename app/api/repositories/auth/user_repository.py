from dataclasses import dataclass
from app.db import db
from app.api.models.auth import User


@dataclass
class UserRepository:

    def find_by_id(self, id: int) -> User | None:
        return db.session.query(User).get(id)

    def find_by_username(self, username: str) -> User | None:
        return db.session.query(User).where(User.username == username).first()

    def find_by_token(self, token: str):
        return db.session.query(User).where(User.token == token).first()

    def logout(self, user: User) -> None:
        user.token = None
        self.save(user)

    def save(self, user: User) -> User:
        if user.id is None:
            db.session.add(user)
        db.session.commit()

        return user
