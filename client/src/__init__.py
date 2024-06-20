from flask import Flask
from flask_login import LoginManager
from server.api.ListaDeContatos.db_connector import DatabaseConnection, config

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'infinity'
    app.config['SQLALCHEMY_DATABASE_URI'] = config

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        # como user_id é a chave primaria da nossa tabela, usamos isso pra pesquisar o usuario existente no banco 
        return User.get_by_id(user_id)
    
    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
