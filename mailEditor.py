#coletar info para email, será coletado de um json #Imaginar que o email vem em um json(dict) para o backend
import json

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

#agendar envio #

#previa do email

#testing:
if __name__ == "__main__":
    print(getSubject())
    print(getBody())




