from Classes.ItemComponente import ItemComponente

class ItemSimples(ItemComponente):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco
