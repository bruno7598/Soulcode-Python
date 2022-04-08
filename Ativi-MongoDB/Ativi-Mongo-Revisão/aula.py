
# -----------------------------------------------------------------------
# INICIO PYTHON 2
# -----------------------------------------------------------------------

# class Funcionario:
    
#     def __init__(self, nome, cpf, salario):
#         self._nome = nome
#         self._cpf = cpf
#         self._salario = salario  
        
#     def get_salario(self):
#         print("Meu salário é: ", self._salario)

#     def get_bonificacao(self): 
#         return self._salario * 0.15 

# f = Funcionario('José', '45678998788',5000.59)
# f.get_salario()
# print(f.get_bonificacao())



# class Animal:
#     def __init__(self, nome, porte):
#         self.nome = nome
#         self.porte = porte
        
# class Gato(Animal): 
#     def __init__(self, nome, porte, som):
#         super().__init__(nome, porte)
#         self.som = som
        

# lex = Gato('Lex', 'Médio', 'Mia')
# lala = Gato('Lala', 'Pequeno', 'Mia')
        
# print(vars(lex))
# print(vars(lala))




# -----------------------------------------------------------------------
# REVERTER
# -----------------------------------------------------------------------

# import reverse as re

# re.revese("12345")






# -----------------------------------------------------------------------
# MONGO
# ----------------------------------------------------------------------- 

# from pymongo import collection

# def get_database():
#     from pymongo import MongoClient

#     CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
#     client = MongoClient(CONNECTION_STRING)
#     print("Conectado com sucesso...")
#     return client['soul_code_data']
    
# dbname = get_database()
# collection_name = dbname["itens_soulcode"]

# item_1 = {
#     "_id":"SC001",
#     "nome_item":"Livro",
#     "desconto_maximo":"10%",
#     "REF":"RRGSFF001",
#     "preco": 340,
#     "categoria":"Físico"
# }

# item_2 = {
#     "_id":"SC002",
#     "nome_item":"Camera",
#     "desconto_maximo":"15%",
#     "REF":"RRGSJ001S4",
#     "preco": 540,
#     "categoria":"Físico"
# }

# item_3 = {
#     "nome_item":"Microfone",
#     "desconto_maximo":"12%",
#     "REF":"RRGSJ0FRSW7854R",
#     "preco": 300,
#     "categoria":"Físico"
# }

# item_4 = {
#     "nome_item":"Aula Remota",
#     "desconto_maximo":"19%",
#     "REF":"RRGS844W7854R",
#     "preco": 400,
#     "categoria":"Online"
# }

# item_5 = {
#     "_id":"SC005",
#     "nome_item":"Apostila",
#     "desconto_maximo":"19%"
# }

# #collection_name.insert_many([item_1,item_2,item_3])
# collection_name.insert_one(item_4)
# collection_name.insert_one(item_5)
# print("Dados inseridos!")




# -----------------------------------------------------------------------
# MONGO
# -----------------------------------------------------------------------


# from pymongo import collection

# def get_database():
#     from pymongo import MongoClient

#     CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
#     client = MongoClient(CONNECTION_STRING)
#     print("Conectado com sucesso...")
#     return client['soul_code_data']
    
# dbname = get_database()
# collection_name = dbname["itens_soulcode"]


# #detalhes_itens = collection_name.find()
# #detalhes_itens = collection_name.find({"categoria":"Online"})
# #detalhes_itens = collection_name.find({"$and" : [{"categoria":"Online"}, {"categoria":"Físico"}]})
# detalhes_itens = collection_name.find({"nome_item":{"$regex":"^Mi"}})
# for item in detalhes_itens:
#     print(item)
# 
# from pymongo import collection

# def get_database():
#     from pymongo import MongoClient

#     CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
#     client = MongoClient(CONNECTION_STRING)
#     print("Conectado com sucesso...")
#     return client['soul_code_data']
    
# dbname = get_database()
# collection_name = dbname["itens_soulcode"]


# #atualiza desconto_maximo de 10% para 35%.
# collection_name.update_many({"disconto_maximo":"10%"}, 
#   {"$set":{"disconto_maximo": "35%"}})

# #atualiza desconto para 100% onde nome_item tenha a palavra 'Aula'
# collection_name.update_one({ "nome_item": { "$regex": "Aula" } },
#  {"$set":{"disconto_maximo": "100%"}})




# detalhes_itens = collection_name.find()
# for item in detalhes_itens:
#    print(item)


# #Exclui documento cujo ID é SC004
# collection_name.delete_one({"_id" : "SC004"})
# #Deeta todos os documentos
# collection_name.drop()
# dbname.drop_collection()





# -----------------------------------------------------------------------
# MONGO
# -----------------------------------------------------------------------

# from pymongo import collection

# def get_database():
#     from pymongo import MongoClient

#     CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
#     client = MongoClient(CONNECTION_STRING)
#     print("Conectado com sucesso...")
#     return client['soul_code_data']

# def cadastrarDocumento():
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']

#     n = int(input("Quantos campos terá seu documento? "))
#     d = dict(input("Digite a chave e o valor separado por espaços: ").split() for _ in range(n))
#     print(d)
#     collection_name.insert_one(d)
#     print("Documento inserido com sucesso!")

# cadastrarDocumento()








# -----------------------------------------------------------------------
# MONGO
# -----------------------------------------------------------------------


# from pymongo import collection

# def get_database():
#     from pymongo import MongoClient

#     CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
#     client = MongoClient(CONNECTION_STRING)
#     print("Conectado com sucesso...")
#     return client['soul_code_data']

# def cadastrarDocumento():
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']

#     n = int(input("Quantos campos terá seu documento? "))
#     d = dict(input("Digite a chave e o valor separado por espaços: ").split() for _ in range(n))
#     print(d)
#     collection_name.insert_one(d)
#     print("Documento inserido com sucesso!")

# def mostrarDocumento():
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']
#     detalhes_itens = collection_name.find()
#     for item in detalhes_itens:
#         print(item)


# #cadastrarDocumento()
# mostrarDocumento()










# -----------------------------------------------------------------------
# MONGO
# -----------------------------------------------------------------------


# from pymongo import collection

# def get_database():
#     from pymongo import MongoClient

#     CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
#     client = MongoClient(CONNECTION_STRING)
#     print("Conectado com sucesso...")
#     return client['soul_code_data']

# def cadastrarDocumento():
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']

#     n = int(input("Quantos campos terá seu documento? "))
#     d = dict(input("Digite a chave e o valor separado por espaços: ").split() for _ in range(n))
#     print(d)
#     collection_name.insert_one(d)
#     print("Documento inserido com sucesso!")

# def mostrarDocumento():
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']
#     detalhes_itens = collection_name.find()
#     for item in detalhes_itens:
#         print(item)

# def deletarDocumento():
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']
#     documento = str(input("Qual o ID do item a ser deletado?"))
#     collection_name.delete_one({"_id":documento})
#     print("Documento exluído com sucesso!")



# #cadastrarDocumento()
# mostrarDocumento()
# #deletarDocumento()




# -----------------------------------------------------------------------
# MONGO
# -----------------------------------------------------------------------

# from pymongo import collection

# def get_database():
#     from pymongo import MongoClient

#     CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
#     client = MongoClient(CONNECTION_STRING)
#     print("Conectado com sucesso...")
#     return client['soul_code_data']

# def cadastrarDocumento():
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']

#     n = int(input("Quantos campos terá seu documento? "))
#     d = dict(input("Digite a chave e o valor separado por espaços: ").split() for _ in range(n))
#     print(d)
#     collection_name.insert_one(d)
#     print("Documento inserido com sucesso!")

# def mostrarDocumento():
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']
#     detalhes_itens = collection_name.find()
#     for item in detalhes_itens:
#         print(item)

# def deletarDocumento():
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']
#     documento = str(input("Qual o ID do item a ser deletado?"))
#     collection_name.delete_one({"_id":documento})
#     print("Documento exluído com sucesso!")

# def deletarTudo():
#     var = str(input("Deseja realmente deletar tudo? S/N"))
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']

#     if (var == 'S'):
#         collection_name.drop()
#         dbname.drop_collection()
#     elif (var=='N'):
#         print("Nenhum dado foi excluído!")


# #cadastrarDocumento()
# #mostrarDocumento()
# #deletarDocumento()
# deletarTudo()



# -----------------------------------------------------------------------
# MONGO
# -----------------------------------------------------------------------

# from pymongo import collection

# def get_database():
#     from pymongo import MongoClient

#     CONNECTION_STRING = "mongodb+srv://root:root@cluster0.tb8hv.mongodb.net/myFirstDatabase"
    
#     client = MongoClient(CONNECTION_STRING)
#     print("Conectado com sucesso...")
#     return client['soul_code_data']

# def cadastrarDocumento():
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']

#     n = int(input("Quantos campos terá seu documento? "))
#     d = dict(input("Digite a chave e o valor separado por espaços: ").split() for _ in range(n))
#     print(d)
#     collection_name.insert_one(d)
#     print("Documento inserido com sucesso!")

# def mostrarDocumento():
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']
#     detalhes_itens = collection_name.find()
#     for item in detalhes_itens:
#         print(item)

# def deletarDocumento():
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']
#     documento = str(input("Qual o ID do item a ser deletado?"))
#     collection_name.delete_one({"_id":documento})
#     print("Documento exluído com sucesso!")

# def deletarTudo():
#     var = str(input("Deseja realmente deletar tudo? S/N"))
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']

#     if (var == 'S'):
#         collection_name.drop()
#         dbname.drop_collection()
#     elif (var=='N'):
#         print("Nenhum dado foi excluído!")

# def atualizarDocumento():
#     dbname = get_database()
#     collection_name = dbname['itens_soulcode']
#     temp = str(input("O que você deseja alterar?\n1-Atualizar por ID: \n2-Atualizar por campo: "))
#     if (temp=="1"):
#         id = str(input("Digite o ID as ser alterado: "))
#         chave = str(input("Digite o campo a ser aletrado: "))
#         valor = str(input("Digite o novo valor do campo digitado: "))

#         collection_name.update_one({"_id":id}, {"$set":{chave:valor}})
#         print("Modificação realizada!")
#     elif (temp=="2"):
#         chave = str(input("Digite a chave a ser buscada: "))
#         valor = str(input("Digite o valor a ser buscado: "))
#         chave2 = str(input("Digite a chave a ser alterada: "))
#         valor2 = str(input("Digite o novo valor: "))

#         collection_name.update_many({chave:valor}, {"$set":{chave2:valor2}})
#         print("Modificação realizada!")

# #cadastrarDocumento()
# #deletarDocumento()
# #deletarTudo()
# atualizarDocumento()
# mostrarDocumento()