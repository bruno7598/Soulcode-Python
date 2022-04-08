from pymongo import database
from modules.conector import Interface_db
from  pymongo.database import Database
import pandas
if __name__ == "__main__":
    
       
    client = Interface_db()
    print(client.collection.find())
    
    # db =  client.soulcode
    
    # db.clientes.insert_one({
    # "nome": "bruno",
    # "cpf": 'test'
    # })   
    
    # a = db.professores.find()

    # for item in a:
    #     for j in item:
    #         print(item[j])