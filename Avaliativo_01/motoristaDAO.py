from database import Database
from motorista import Motorista

class MotoristaDAO:
    def __init__(self, database: Database):
        self.db = database

    def criar_motorista(self, motorista: Motorista):
        try:
            self.db.collection.insert_one(motorista.to_dict())
            print(f"Motorista {motorista.nome} criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar motorista: {e}")

    def ler_motorista(self, nome: str):
        try:
            motorista = self.db.collection.find_one({"nome": nome})
            if motorista:
                return motorista
            else:
                print(f"Motorista {nome} não encontrado.")
        except Exception as e:
            print(f"Erro ao ler motorista: {e}")

    def atualizar_motorista(self, nome: str, novos_dados: dict):
        try:
            self.db.collection.update_one({"nome": nome}, {"$set": novos_dados})
            print(f"Motorista {nome} atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar motorista: {e}")

    def deletar_motorista(self, nome: str):
        try:
            self.db.collection.delete_one({"nome": nome})
            print(f"Motorista {nome} deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar motorista: {e}")
