from Restaurante import Restaurante
from ItemCardapio import ItemCardapio

class Pedido:
    def __init__(self, restaurante: Restaurante):
        self.restaurante = restaurante
        self.itens = []

    def adicionar_item(self, item: ItemCardapio):
        self.itens.append(item)

    def remover_item(self, item: ItemCardapio):
        self.itens.remove(item)

    def resumo(self):
        total = sum(item.preco for item in self.itens)
        print("\nResumo do Pedido:")
        for item in self.itens:
            print(f" - {item}")
        print(f"Total a pagar: R$ {total:.2f}\n")
        return total