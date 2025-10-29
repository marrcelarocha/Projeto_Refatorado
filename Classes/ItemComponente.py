from abc import ABC, abstractmethod

class ItemComponente(ABC):
    @abstractmethod
    def get_nome(self):
        pass

    @abstractmethod
    def get_preco(self):
        pass

    def exibir_detalhes(self, nivel=0):
        indent = "  " * nivel
        print(f"{indent}- {self.get_nome()}: R${self.get_preco():.2f}")
