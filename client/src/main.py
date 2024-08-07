from flask import Blueprint
from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint("main", __name__)


@main.route("/")
def inicio():
    if current_user.is_authenticated:
        return render_template("inicio.html", name=current_user.username)
    else:
        return render_template("inicio.html", name="Convidado")


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html", name=current_user.username)


@main.route("/email")
def email():
    return render_template("emailEditor.html", name=current_user.username)


# criação inicial colocar autenticação
@main.route("/agendamento")
@login_required
def agendamento():
    return render_template("scheduled.html", name=current_user.username)


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
