##Product class (interface)
from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, descricao):
        self._descricao = descricao

    @property
    def descricao(self):
        return self._descricao

    @abstractmethod
    def processar(self, valor):
        pass


##Concrete products

class PagamentoPix(Pagamento):
    def __init__(self, chave_pix):
        super().__init__("Pagamento via PIX")
        self._chave_pix = chave_pix

    @property
    def chave_pix(self):
        return self._chave_pix

    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado via PIX.")
        print(f"Chave PIX: {self._chave_pix}")
        print(f"Descrição: {self._descricao}\n")

class PagamentoCartao(Pagamento):
    def __init__(self, numero_cartao, titular, cvv):
        super().__init__("Pagamento no Cartão")
        self._numero_cartao = numero_cartao
        self._titular = titular
        self._cvv = cvv

    @property
    def numero_cartao(self):
        return self._numero_cartao

    @property
    def titular(self):
        return self._titular

    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado no Cartão.")
        print(f"Cartão: **** **** **** {self._numero_cartao[-4:]}")
        print(f"Titular: {self._titular}")
        print(f"Descrição: {self._descricao}\n")

##Creator

class PagamentoFactory(ABC):
    @abstractmethod
    def criar_pagamento(self) -> Pagamento:
        pass


##Concrete creators

class PagamentoPixFactory(PagamentoFactory):
    def __init__(self, chave_pix):
        self.chave_pix = chave_pix

    def criar_pagamento(self):
        return PagamentoPix(self.chave_pix)
    
class PagamentoCartaoFactory(PagamentoFactory):
    def __init__(self, numero_cartao, titular, cvv):
        self.numero_cartao = numero_cartao
        self.titular = titular
        self.cvv = cvv

    def criar_pagamento(self):
        return PagamentoCartao(self.numero_cartao, self.titular, self.cvv)



##        if metodo == "pix":
##            chave = input("Digite sua chave PIX: ").strip()
##            fabrica = PagamentoPixFactory(chave)
##        elif metodo == "cartao":
##            numero = input("Número do cartão: ").strip()
##            titular = input("Titular do cartão: ").strip()
##            cvv = input("CVV: ").strip()
##            fabrica = PagamentoCartaoFactory(numero, titular, cvv)
##        else:
##            print("Método inválido, pedido cancelado.\n")
##            return
        
##        pagamento = fabrica.criar_pagamento()        
        
##        pagamento.processar(total)
##        self.simular_entrega(restaurante)
