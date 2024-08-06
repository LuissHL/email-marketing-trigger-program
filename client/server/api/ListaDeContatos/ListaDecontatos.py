from db_helper import DBHelper
import json

conn = DBHelper()


def ListarContatos():
    contatos = conn.execute(
        "SELECT cf.id, cf.Nome_Cliente_Funcionario, cf.Senha, cf.Tipo, cf.Area, e.Endereço_Email FROM ClienteFuncionario cf JOIN Email e ON cf.Email_ID = e.id"
    )
    contatos_json = []
    for user in contatos:
        contato = {
            "id": user[0],
            "nome": user[1],
            "senha": user[2],
            "tipo": user[3],
            "area": user[4],
            "email": user[5],
        }
        contatos_json.append(contato)
    return contatos_json


contatos_json = ListarContatos()

json_contatos = json.dumps(contatos_json)
print(json_contatos)
