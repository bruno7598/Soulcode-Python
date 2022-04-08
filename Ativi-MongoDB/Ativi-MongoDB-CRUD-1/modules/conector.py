import collections
from pymongo import MongoClient

class Interface_db:
    client = ''
    database = ''
    collection = ''
    
    
    
    def __init__(self, host="mongodb://127.0.0.1:27017/",database="soulcode",collection="professores"):
        self.client = MongoClient(host)
        self.database = database
        self.collection = collection
        
    def set_database(self, database):
        self.database = database
    
    def set_collection(self, collection):
        self.collection = collection
        
    