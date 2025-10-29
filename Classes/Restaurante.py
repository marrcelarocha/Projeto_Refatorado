from Classes.ItemSimples import ItemSimples
from Classes.ItemCombo import Combo
from Classes.ItemComponente import ItemComponente

class Restaurante:
    def __init__(self, nome, categoria):
        self._nome = nome.lower().strip()
        self._categoria = categoria
        self.cardapio: list[ItemComponente] = []

    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    def adicionar_item(self, item: ItemComponente):
        if any(i.get_nome().lower() == item.get_nome().lower() for i in self.cardapio):
            print("Este item já existe no cardápio.\n")
            return
        self.cardapio.append(item)
        print(f"Item '{item.get_nome()}' adicionado ao cardápio de {self._nome}.\n")

    def remover_item(self, nome_item):
        for item in self.cardapio:
            if item.get_nome().lower() == nome_item.lower():
                self.cardapio.remove(item)
                print(f"Item '{nome_item}' removido.\n")
                return
        print("Item não encontrado.\n")

    def exibir_cardapio(self):
        if not self.cardapio:
            print("Cardápio vazio.\n")
            return
        print(f"\nCardápio de {self._nome.capitalize()}:")
        for item in self.cardapio:
            item.exibir_detalhes()
        print()

    # === NOVOS MÉTODOS DO COMPOSITE ===
    def criar_item_simples(self):
        nome = input("Nome do prato: ").strip()
        preco = float(input("Preço: "))
        item = ItemSimples(nome, preco)
        self.adicionar_item(item)

    def criar_combo(self):
        nome_combo = input("Nome do combo: ").strip()
        combo = Combo(nome_combo)
        print("Adicione os itens ao combo (digite 'fim' para encerrar):")

        while True:
            nome_item = input("Item: ").strip()
            if nome_item.lower() == "fim":
                break

            item_existente = next((i for i in self.cardapio if i.get_nome().lower() == nome_item.lower()), None)
            if item_existente:
                combo.adicionar_item(item_existente)
            else:
                print("Item não encontrado no cardápio.")

        self.adicionar_item(combo)
        print(f"Combo '{nome_combo}' criado com sucesso!\n")

    def detalhes(self):
        print(f"\nNome: {self._nome.capitalize()}")
        print(f"Categoria: {self._categoria}")
        if not self.cardapio:
            print("Cardápio vazio.")
        else:
            print("Cardápio:")
            for item in self.cardapio:
                item.exibir_detalhes()
        print()
