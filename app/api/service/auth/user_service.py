from dataclasses import dataclass
from app.errors import DomainError, NotFoundError
from app.api.repositories.auth import UserRepository
from app.api.models.auth import User


@dataclass
class UserService:
    user_repository: UserRepository

    def find_by_id(self, user_id: int) -> User:
        user = self.user_repository.find_by_id(user_id)

        if user is None:
            raise NotFoundError("Usuário não encontrado")

        return user

    def create(self, user: User) -> User:
        existent_user = self.user_repository.find_by_username(user.username)

        if existent_user is not None:
            raise DomainError("Usuário já cadastrado.")

        user = self.user_repository.save(user)
        return user
