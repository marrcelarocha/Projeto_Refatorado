from Classes.ItemCardapio import ItemCardapio

class Restaurante:
    def __init__(self, nome, categoria):
        self._nome = nome.lower().strip()
        self._categoria = categoria
        self.cardapio = []

    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    def adicionar_item(self, item: ItemCardapio):
        if any(i.nome == item.nome for i in self.cardapio):
            print("Este item já existe no cardápio.\n")
            return
        self.cardapio.append(item)
        print(f"Item '{item.nome}' adicionado ao cardápio de {self._nome}.\n")

    def remover_item(self, nome_item):
        for item in self.cardapio:
            if item.nome == nome_item:
                self.cardapio.remove(item)
                print(f"Item '{nome_item}' removido.\n")
                return
        print("Item não encontrado.\n")

    def exibir_cardapio(self):
        if not self.cardapio:
            print("Cardápio vazio.\n")
            return
        print(f"Cardápio de {self._nome.capitalize()}:")
        for item in self.cardapio:
            print(f" - {item}")
        print()

    def detalhes(self):
        print(f"\nNome: {self._nome.capitalize()}")
        print(f"Categoria: {self._categoria}")
        if not self.cardapio:
            print("Cardápio vazio.")
        else:
            print("Cardápio:")
            for item in self.cardapio:
                print(f" - {item}")
        print()
