import pymysql.cursors

class data:
    def __init__(self):
        self.conexao = pymysql.connect(host='localhost',
                                       user='root',
                                       password='',
                                       database='xxxx', #colocar o nome da base de dados
                                       cursorclass=pymysql.cursors.DictCursor)


    def getSegment(self):
        segment = input("Qual segmento?") #input somente para teste, em producao essa info bem do front e precisar catar ela na BD
        with self.conexao.cursor() as cursor:
            sql = f"SELECT `{segment}` FROM segments" #alterar nome do item e da base de dados depois
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
        


if __name__ == "__main__":
    data.getsegment()