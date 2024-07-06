# # TESTE PARA IMPORTAR CSV, LISTA DE CONTATOS
# import csv
# import os
# #Programa so roda se estiver no diretorio correto isso pode ser um problema
# try:
#     file_path = "contacts.csv"  # Talvez seja precisa mudar o path para algum absoluto
#     print(f"Current working directory: {os.getcwd()}")
#     with open(file_path, mode='r') as file:
#         csvreader = csv.reader(file)
#         header = next(csvreader)
#         print(header)
#         rows = []
#         for row in csvreader:
#             rows.append(row)
#         print(rows)
# except FileNotFoundError as e:
#     print(f"Error: {e}")

# segundo metodo
import pandas as pd
db_test ={}
names =[]
emails=[]
roles=[]

data = pd.read_csv("contacts.csv")
print("\n")
print(data.head)
print("\n")

for i in data.Name:
  print(i)
  names.append(i)

for i in data.Email:
  print(i)
  emails.append(i)

for i in data.Role:
  print(i)
  roles.append(i)

print(f"{names};\n{emails};\n{roles};\n")

# SQL function :
#   for i in range(lista): 
#     INSERT INTO cliente({name,email,role)
#     VALUES (f"[names[i],[emails[i],[roles[i]")