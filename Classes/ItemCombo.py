from Classes.ItemComponente import ItemComponente

class Combo(ItemComponente):
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar_item(self, item: ItemComponente):
        self.itens.append(item)

    def remover_item(self, item: ItemComponente):
        self.itens.remove(item)

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return sum(item.get_preco() for item in self.itens)

    def exibir_detalhes(self, nivel=0):
        indent = "  " * nivel
        print(f"{indent}+ {self.get_nome()} (Combo): R${self.get_preco():.2f}")
        for item in self.itens:
            item.exibir_detalhes(nivel + 1)
