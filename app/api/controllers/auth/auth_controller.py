from apiflask import APIBlueprint
from app.api.security import auth, JwtService
from app.api.models.auth import User
from app.api.schemas.auth import UserIn
from app.api.service.auth import AuthService
from app.api.repositories.auth import UserRepository


auth_bp = APIBlueprint("Autentication", __name__, url_prefix="/api/auth")


@auth_bp.post("/login")
@auth_bp.input(UserIn, arg_name="credentials")
def login(
    credentials: dict,
    auth_service: AuthService = AuthService(UserRepository(), JwtService()),
):
    token: str = auth_service.login(
        credentials.get("username"), credentials.get("password")
    )

    return {"type": "bearer", "access_token": token}


@auth_bp.delete("/logout")
@auth_bp.auth_required(auth)
def logout(auth_service: AuthService = AuthService(UserRepository(), JwtService())):
    current_user: User = auth.current_user
    auth_service.logout(current_user)
    return {"message": "Usuário desconectado com sucesso."}
