from apiflask import APIBlueprint
from app.api.security import auth
from app.api.schemas.auth import UserIn, UserOut
from app.api.service.auth import UserService
from app.api.repositories.auth import UserRepository
from app.api.models.auth import User


user_bp = APIBlueprint("Usuários", __name__, url_prefix="/api/user")


@user_bp.get("/me")
@user_bp.output(UserOut)
@user_bp.auth_required(auth)
def get_current_user():
    return auth.current_user


@user_bp.get("/<int:id>")
@user_bp.output(UserOut)
@user_bp.auth_required(auth, roles=["admin"])
def find_user_by_id(id: int, user_service: UserService = UserService(UserRepository())):
    return user_service.find_by_id(id)


@user_bp.post("/")
@user_bp.input(UserIn, arg_name="new_user")
@user_bp.auth_required(auth, roles=["admin"])
def create_new_user(
    new_user: dict, user_service: UserService = UserService(UserRepository())
):
    new_user: User = User(new_user.get("username"), new_user.get("password"))
    user_service.create(new_user)
    return {"message": "Usuário cadastrado com sucesso."}
