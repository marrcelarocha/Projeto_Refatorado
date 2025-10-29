from Classes.Restaurante import Restaurante
from Classes.ItemComponente import ItemComponente
from Classes.State import (AguardandoPagamento,
                           EstadoPedido,
                           Preparando,
                           Entregue)
from Classes.Observer import PedidoNotifier
from Classes.Strategy import (Contexto, PrimeiraCompra, Cupom10, Cupom25)

# CONTEXT (STRATEGY)
# COMPONENTE CONCRETO (DECORATOR)
class Pedido():
    def __init__(self, restaurante: Restaurante):
        self.restaurante = restaurante
        self.itens = []
        self.estado = AguardandoPagamento()
        self.notifier = PedidoNotifier()

    def adicionar_item(self, item: ItemComponente):
        self.itens.append(item)

    def remover_item(self, item: ItemComponente):
        self.itens.remove(item)

    def avancar_estado(self):
        self.estado.avancar(self)

    def resumo(self):
        total = sum(item.get_preco() for item in self.itens)

        print("Escolha alguma promoção:")
        print("1 - PRIMEIRACOMPRA")
        print("2 - CUPOM10")
        print("3 - CUPOM25")

        promocao = input("Digite o número da promoção: ")
        contexto = Contexto()
        if promocao == "1":
            contexto.strategy = PrimeiraCompra()
        elif promocao == "2":
            contexto.strategy = Cupom10()
        elif promocao == "3":
            contexto.strategy = Cupom25()
        else:
            print("Promoção inválida, sem desconto aplicado.")
            resultado = total
            return resultado

        resultado = contexto.executar_strategy(total)

        print("\nResumo do Pedido:")
        for item in self.itens:
            print(f" - {item}")
        print(f"Total sem desconto: R$ {total:.2f}\n")
        print(f"Total com desconto: R$ {resultado:.2f}\n")
        return resultado
    
    def preco(self):
        return sum(item.get_preco() for item in self.itens)