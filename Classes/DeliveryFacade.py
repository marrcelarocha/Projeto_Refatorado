from Classes.SistemaDeDelivery import SistemaDelivery
from Classes.Pedido import Pedido
from Classes.Observer import NotificacaoUsuario, NotificacaoRestaurante
from Classes.ItemComponente import ItemComponente
from Classes.Excecoes import DeliveryError

class DeliveryFacade:
    def __init__(self):
        self.sistema = SistemaDelivery.get_instancia()

    # --- RESTAURANTES ---
    def cadastrar_restaurante(self, nome, categoria):
        self.sistema.cadastrar_restaurante(nome, categoria)

    def listar_restaurantes(self):
        self.sistema.listar_restaurantes()

    def buscar_restaurante(self, nome):
        return self.sistema.buscar_restaurante(nome)

    def exibir_cardapio(self, nome_rest):
        rest = self.sistema.buscar_restaurante(nome_rest)
        if rest:
            rest.exibir_cardapio()
        else:
            print("Restaurante não encontrado.\n")

    def adicionar_item_cardapio(self, nome_rest, item, preco):
        rest = self.sistema.buscar_restaurante(nome_rest)
        if rest:
            rest.adicionar_item(ItemComponente(item, preco)) 
        else:
            print("Restaurante não encontrado.\n")

    # --- USUÁRIOS ---
    def cadastrar_usuario(self):
        self.sistema.cadastrar_usuario()

    def login(self):
        return self.sistema.processar_login()

    # --- PEDIDOS ---
    def criar_pedido(self, user, restaurante):
        pedido = Pedido(restaurante)
        pedido.notifier.adicionar_subscriber(NotificacaoUsuario())
        pedido.notifier.adicionar_subscriber(NotificacaoRestaurante())
        return pedido

    def adicionar_item_pedido(self, pedido, item: ItemComponente):
        if not isinstance(item, ItemComponente):
            raise TypeError("Apenas objetos do tipo ItemComponente podem ser adicionados")
        pedido.adicionar_item(item)
        print(f"{item.get_nome()} adicionado ao pedido!\n")  # agora usa get_nome() do Composite

    def remover_item_pedido(self, pedido, item: ItemComponente):
        pedido.remover_item(item)

    def finalizar_pedido(self, pedido):
        try:
            self.sistema.fazer_pedido(pedido)

        except DeliveryError as e:
            print(f"[ERRO] Falha ao finalizar pedido: {e}")
            return

        else:
            # só executa se nenhuma exceção ocorreu
            pedido.avancar_estado()
            pedido.avancar_estado()
            self.sistema.simular_entrega(pedido.restaurante)