from corrida import Corrida
from motoristaDAO import MotoristaDAO
from passageiro import Passageiro
from motorista import Motorista


class MotoristaCLI:
    def __init__(self, motorista_dao: MotoristaDAO):
        self.motorista_dao = motorista_dao

    def menu(self):
        while True:
            print("\n1. Criar Motorista")
            print("2. Ler Motorista")
            print("3. Atualizar Motorista")
            print("4. Deletar Motorista")
            print("5. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.criar_motorista()
            elif escolha == "2":
                self.ler_motorista()
            elif escolha == "3":
                self.atualizar_motorista()
            elif escolha == "4":
                self.deletar_motorista()
            elif escolha == "5":
                print("\n1. Até mais!!")
                break
            else:
                print("Opção inválida!")

    def criar_motorista(self):
        nome = input("Nome do motorista: ")
        nota = float(input("Nota do motorista (0 a 10): "))
        corridas = []

        while True:
            print("Adicionando corrida...")
            nota_corrida = float(input("Nota da corrida (0 a 10): "))
            distancia = float(input("Distância da corrida (km): "))
            valor = float(input("Valor da corrida: "))
            nome_passageiro = input("Nome do passageiro: ")
            documento_passageiro = input("Documento do passageiro: ")

            passageiro = Passageiro(nome_passageiro, documento_passageiro)
            corrida = Corrida(nota_corrida, distancia, valor, passageiro)
            corridas.append(corrida)

            continuar = input("Adicionar mais uma corrida? (s/n): ")
            if continuar.lower() != 's':
                break

        motorista = Motorista(nome, nota, corridas)
        self.motorista_dao.criar_motorista(motorista)

    def ler_motorista(self):
        nome = input("Nome do motorista a ser lido: ")
        motorista = self.motorista_dao.ler_motorista(nome)
        if motorista:
            print(motorista)

    def atualizar_motorista(self):
        nome = input("Nome do motorista a ser atualizado: ")
        novos_dados = {}
        novos_dados["nome"] = input("Novo nome do motorista (ou pressione Enter para manter o mesmo): ")
        novos_dados["nota"] = float(input("Nova nota do motorista (ou pressione Enter para manter a mesma): ") or 0)
        self.motorista_dao.atualizar_motorista(nome, novos_dados)

    def deletar_motorista(self):
        nome = input("Nome do motorista a ser deletado: ")
        self.motorista_dao.deletar_motorista(nome)
