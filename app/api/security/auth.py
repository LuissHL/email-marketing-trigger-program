from apiflask import HTTPTokenAuth

# from jose import ExpiredSignatureError, JWTError
from app.errors import UnauthorizedError
from app.api.models.auth import User
from app.api.repositories.auth import UserRepository
from app.api.security.jwt import JwtService


auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(
    token: str,
    jwt_service: JwtService = JwtService(),
    user_repository: UserRepository = UserRepository(),
) -> User:
    if not token:
        raise UnauthorizedError("Token inválido")

    user: User = user_repository.find_by_token(token)

    if user is None:
        raise UnauthorizedError("Token expirado.")

    try:
        jwt_service.decode_token(token)
    except:
        user_repository.logout(user)
        raise UnauthorizedError("Token expirado.")
    # except:
    #     raise UnauthorizedError("Token inválido.")

    return user


@auth.get_user_roles
def get_user_roles(user: User) -> list[str]:
    return user.get_user_roles()
