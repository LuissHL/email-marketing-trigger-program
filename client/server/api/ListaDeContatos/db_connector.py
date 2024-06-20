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
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'forever@',
    'database':'disparoDeEmail',
}