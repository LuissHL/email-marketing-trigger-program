import mysql.connector


class DatabaseConnection:
    def __init__(self, config):
        self.config = config
        self.connection = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.config)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

    def fetch_as_list(cursor):#select
        return [list(row) for row in cursor.fetchall()] #list comprehension
    
    def fetch_as_dict(cursor):#select
        columns = cursor.column_names
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
#O Config é o acesso para o banco de dados varia de cada um, mais o xamp tem um padrão que esse.
config = {
    'user': 'root',  # Nome de usuário padrão do MySQL no XAMPP
    'password': '',  # Senha vazia por padrão no XAMPP
    'host': 'localhost',  # Host padrão no XAMPP
    'database': 'appemail',  # Nome do banco de dados
    'raise_on_warnings': True  # Opção para levantar exceções em caso de alertas
}