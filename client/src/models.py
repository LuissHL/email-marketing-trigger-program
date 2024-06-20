from flask import current_app
from server.api.ListaDeContatos.db_connector import DatabaseConnection

# o modelo com quais os atributos que um usuario criado terá
class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

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
