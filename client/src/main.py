from flask import Blueprint
from . import db
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('inicio.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')







"""


from flask import Flask, request, jsonify
from auth import UserCredentials, create_token, authenticate_user, token_required

app = Flask(__name__)

# Endpoint protegido por autenticação.
@app.route('/me', methods=['GET'])
@token_required
def me(authenticated_user):
    return jsonify(authenticated_user)

# Endpoint para realizar o login.
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    credentials = UserCredentials(**data)
    token = create_token(credentials.username, credentials.password)
    
    if isinstance(token, tuple):
        return token  # Retorna a resposta de erro se houver
    
    return jsonify({
        'access-token': token,
        'type': 'Bearer'
    })

if __name__ == '__main__':
    app.run(debug=True)
"""