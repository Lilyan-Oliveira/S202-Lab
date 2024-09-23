from corrida import Corrida

class Motorista:
    def __init__(self, nome: str, nota: float, corridas: list[Corrida]):
        self.nome = nome
        self.nota = nota
        self.corridas = corridas

    def to_dict(self):
        return {
            "nome": self.nome,
            "nota": self.nota,
            "corridas": [corrida.to_dict() for corrida in self.corridas]
        }
