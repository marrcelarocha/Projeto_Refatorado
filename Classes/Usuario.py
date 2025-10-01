from ItemCardapio import ItemCardapio

## produto final
class Usuario:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self._senha = senha
        self.carrinho = []
        ## atributos para o builder
        self.endereco = None
        self.telefone = None
        self.historico_pedidos = []

    ## metódo para adicionar endereço
    def definir_endereco(self, endereco):
        self.endereco = endereco
    
    ## método para adicionar telefone
    def definir_telefone(self, telefone):
        self.telefone = telefone
    
    ## método para adicionar um pedido ao histórico
    def definir_historico(self, pedido):
        self.historico_pedidos.append(pedido)


    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, valor):
        self._senha = valor
    
    def adicionar_item(self, item: ItemCardapio):
        if isinstance(item, ItemCardapio):
            self.carrinho.append(item)
            print(f"Item '{item.nome}' adicionado ao carrinho!\n")
        else:
            print("Erro: apenas objetos ItemCardapio podem ser adicionados.\n")

    def remover_item(self, item: ItemCardapio):
        if item in self.carrinho:
            self.carrinho.remove(item)
            print(f"Item '{item.nome}' removido do carrinho!\n")
        else:
            print(f"Item '{item.nome}' não está no carrinho.\n")

    def exibir_carrinho(self):
        if not self.carrinho:
            print("Carrinho vazio.\n")
            return
        print(f"Carrinho de {self.nome.capitalize()}:")
        for item in self.carrinho:
            print(f" - {item}")
        print()

    def avaliar_prato(self):
        print("\nQual prato você gostaria de avaliar?")
        for item in self.carrinho:
            print(f" - {item}")
        print()
        comida = input("\nDigite o nome do prato: ")
        ranking = input("Avalie de 1 a 5: ")
        comentario = input("Comentário: ")



