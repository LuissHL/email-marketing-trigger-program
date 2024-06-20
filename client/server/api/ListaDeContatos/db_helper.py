from db_connector import DatabaseConnection, config

class DBHelper():
    def __init__(self):
        self.connection = None

    def execute(self, sql):
        with DatabaseConnection(config) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            if sql.split()[0].upper() =='SELECT':
                result = list()          
                for row in cursor.fetchall():
                    result.append(row)
                connection.commit() # APLICAR ALTERAÇÕES (SALVAR)
                cursor.close()
                return result
            else:
                connection.commit()
                cursor.close()
                return None
