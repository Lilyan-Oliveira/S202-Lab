import pymongo
from dataset import motoristas  

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "mongodb+srv://root:root@avaliativo1.87hh0.mongodb.net"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(f"Erro de conexão: {e}")

    def resetDatabase(self):
        try:
            # Apagar os dados antigos da coleção
            self.collection.drop()  # Usar drop em vez de drop_collection
            # Inserir os dados predefinidos
            self.collection.insert_many(motoristas)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(f"Erro ao resetar o banco de dados: {e}")
