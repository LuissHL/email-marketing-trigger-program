from flask import current_app
from server.api.ListaDeContatos.db_connector import DatabaseConnection
from flask_login import UserMixin ,current_user

# o modelo com quais os atributos que um usuario criado terá
class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
    
    @property
    def is_authenticated(self):
        # Implemente a lógica para verificar se o usuário está autenticado
        return True  # Por exemplo, retorne True se o usuário estiver autenticado
    
    @property
    def is_active(self):
        # Implemente a lógica para determinar se o usuário está ativo ou não
        return True
    
    def get_id(self):
      return str(self.id)

    @staticmethod
    def get_by_id(user_id):
        config = current_app.config['DATABASE_CONFIG']
        with DatabaseConnection(config) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, username, email, password FROM users WHERE id = %s", (user_id,))
            result = cursor.fetchone()
            if result:
                return User(*result)
            return None
