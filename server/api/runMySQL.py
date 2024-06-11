from ListaDeContatos.db_connector import DatabaseConnection
class data:
    def __init__(self):
        self.conexao = DatabaseConnection.__enter__

    def getSegment(self):
        segment = input("Qual segmento?") #input somente para teste, em producao essa info bem do front e precisar catar ela na BD
        with self.conexao.cursor() as cursor:
            sql = f"SELECT `{segment}` FROM segments" #alterar nome do item e da base de dados depois
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
        


if __name__ == "__main__":
    data.getsegment()