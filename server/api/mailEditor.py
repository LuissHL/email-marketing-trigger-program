#coletar info para email, será coletado de um json #Imaginar que o email vem em um json(dict) para o backend
import json
from .db_helper import DBHelper

def getSubject():
    openFile = open('emailInfo.json')
    data = json.load(openFile)
    email_subject =str(data["subject"])
    openFile.close()
    return email_subject
def getBody():
    openFile = open('emailInfo.json')
    data = json.load(openFile)
    email_body = str(data["body"])
    openFile.close()
    return email_body

#escolher segmento # coletar da DB
def getSegment():
    connection = DBHelper()
    getSegment  = connection.execute("SELECT cf.id, cf.Tipo, FROM ClienteFuncionario cf JOIN Email e ON cf.Email_ID = e.id") #CF abreviação para Cliente_funcionario
    return getSegment

#transforma o segmento em um lista de contatos
def getRecipients(): 
    recipients= getSegment() #como esses dados virao do bando de dados?
    return recipients


#agendar envio #



#previa do email

#testing:
if __name__ == "__main__":
    print(getSubject())
    print(getBody())



