from dataclasses import dataclass
from datetime import timedelta, datetime as dt, timezone
from app.api.models.auth import User
from app.api.repositories.auth import UserRepository
from app.api.security import JwtService
from app.errors import UnauthorizedError


@dataclass
class AuthService:
    user_repository: UserRepository
    jwt_service: JwtService

    def login(self, username: str, password: str) -> str:
        user: User = self.user_repository.find_by_username(username)

        if user is None or user.verify_password_hash(password) is False:
            raise UnauthorizedError("Credenciais Inválidas.")

        initiated_at: dt = dt.now(timezone.utc)
        token_payload = {
            "iat": initiated_at,
            "exp": initiated_at + timedelta(days=1),
            "user_id": user.id,
        }

        token: str = self.jwt_service.encode_token(token_payload)
        user.token = token
        self.user_repository.save(user)

        return token

    def logout(self, user: User) -> None:
        self.user_repository.logout(user)
