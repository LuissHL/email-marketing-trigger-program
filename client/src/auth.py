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

      

