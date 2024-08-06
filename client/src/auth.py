from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    current_app,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from server.api.ListaDeContatos.db_connector import DatabaseConnection


auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html", name="Convidado")


@auth.route("/signup")
def signup():
    return render_template("signup.html", name="Convidado")


@auth.route("/signup", methods=["POST"])
def sighup_post():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")

    config = current_app.config["DATABASE_CONFIG"]

    with DatabaseConnection(config) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        user = (
            cursor.fetchone()
        )  # if this returns a user, then the email already exists in database

    if (
        user
    ):  # if a user is found, we want to redirect back to signup page so user can try again
        flash("Email address already exists")
        return redirect(url_for("auth.signup"))

    # cria um novo usuário com os dados do formulário. Hash a senha para que a versão em texto simples não seja salva.
    hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
    with DatabaseConnection(config) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, hashed_password),
        )
        connection.commit()
        flash("User successfully created!")

    return redirect(url_for("auth.login"))


@auth.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    config = current_app.config["DATABASE_CONFIG"]

    with DatabaseConnection(config) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, username, email, password FROM users WHERE email = %s", (email,)
        )
        user = cursor.fetchone()

        # verifica se o usuário realmente existe
        # pega a senha fornecida pelo usuário, faz o hash e compara com a senha hash no banco de dados
        if not user or not check_password_hash(user[3], password):
            flash("Please check your login details and try again.")
            return redirect(
                url_for("auth.login")
            )  # se o usuário não existir ou a senha estiver errada, recarregue a página

    # se não passa no if, sabemos que o usuario está com as credenciais certass
    # Aqui passamos os atributos explicitamente para o construtor do User
    user_obj = User(id=user[0], username=user[1], email=user[2], password=user[3])
    login_user(user_obj, remember=remember)

    return redirect(url_for("main.profile"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.inicio"))


"""

from functools import wraps
from flask import request, jsonify
from jose import jwt, ExpiredSignatureError, JWTError
from datetime import datetime as dt, timedelta
from pydantic import BaseModel
from users import get_users_by_username, users
from http import HTTPStatus

# ---------------------------------------------------------------
# Schemas
class UserCredentials(BaseModel):
    username: str 
    password: str

# ---------------------------------------------------------------
# Chave secreta para encryptar e decryptar
ALGORITMO = 'HS256'
SUPER_SECRET_KEY = 'chave_muito_secreta'

# ---------------------------------------------------------------
# JWT Tokens
# Criando o Token
EXPIRATION_TIME = timedelta(hours=3)
def create_token(username: str, password: str) -> str:
    user_id, user = get_users_by_username(username)

    if user is None or user.get('password') != password:
        return jsonify({'detail': 'Credenciais Inválidas.'}), HTTPStatus.UNAUTHORIZED

    initiated_at: dt = dt.utcnow()
    expires_on: dt = initiated_at + EXPIRATION_TIME
    token_payload = {
        'exp': expires_on, 
        'iat': initiated_at, 
        'user_id': user_id
    }

    return jwt.encode(token_payload, SUPER_SECRET_KEY, ALGORITMO)

def authenticate_user(auth_header):
    if not auth_header:
        return jsonify({'detail': 'Token ausente.'}), HTTPStatus.UNAUTHORIZED

    try:
        token = auth_header.split(" ")[1]
        token_payload: dict = jwt.decode(token, SUPER_SECRET_KEY, ALGORITMO)
    except ExpiredSignatureError:
        return jsonify({'detail': 'Token Expirado.'}), HTTPStatus.UNAUTHORIZED
    except JWTError:
        return jsonify({'detail': 'Token inválido.'}), HTTPStatus.UNAUTHORIZED
    
    authenticated_user: dict = users.get(token_payload.get('user_id'))
    authenticated_user.pop('password')
    return authenticated_user

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        authenticated_user = authenticate_user(auth_header)
        if isinstance(authenticated_user, tuple):
            return authenticated_user  # Retorna a resposta de erro se houver
        return f(authenticated_user, *args, **kwargs)
    return decorated

"""
