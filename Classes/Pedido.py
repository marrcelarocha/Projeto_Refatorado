from Classes.Restaurante import Restaurante
from Classes.ItemCardapio import ItemCardapio
from Classes.State import (AguardandoPagamento,
                           EstadoPedido,
                           Preparando,
                           Entregue)
from Classes.Observer import PedidoNotifier

# context
class Pedido:
    def __init__(self, restaurante: Restaurante):
        self.restaurante = restaurante
        self.itens = []
        self.estado = AguardandoPagamento()
        self.notifier = PedidoNotifier()

    def adicionar_item(self, item: ItemCardapio):
        self.itens.append(item)

    def remover_item(self, item: ItemCardapio):
        self.itens.remove(item)

    def avancar_estado(self):
        self.estado.avancar(self)

    def resumo(self):
        total = sum(item.preco for item in self.itens)
        print("\nResumo do Pedido:")
        for item in self.itens:
            print(f" - {item}")
        print(f"Total a pagar: R$ {total:.2f}\n")
        return total