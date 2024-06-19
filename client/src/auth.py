from . import db
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return 'Logout'
    
@auth.route('/sighup', methods=['POST'])
def sighup():
        # code to validate and add user to database goes here
        return redirect(url_for('auth.login'))
@auth.route('/sighup', methods=['POST'])
def sighup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

if user: # if a user is found, we want to redirect back to signup page so user can try again
   flash('Email address already exists')
   return redirect(url_for('auth.sighup')) 

# create a new user with the form data. Hash the password so the plaintext version isn't saved.
new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

# add the new user to the database
db.session.add(new_user)
db.session.commit()

return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page


    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('main.profile'))







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

