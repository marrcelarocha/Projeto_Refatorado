class StrategyInterface:
    def executar_promocao(self, total):
        pass

class PrimeiraCompra(StrategyInterface):
    def executar_promocao(self, total):
        return total * 0.8

class Cupom10(StrategyInterface):
    def executar_promocao(self, total):
        return total * 0.9
    
class Cupom25(StrategyInterface):
    def executar_promocao(self, total):
        return total * 0.75
    
class Contexto:
    def __init__(self):
        self.__strategy = None

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, new_strategy):
        self.__strategy = new_strategy

    def executar_strategy(self, total):
        return self.__strategy.executar_promocao(total)
    

