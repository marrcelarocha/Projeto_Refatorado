from Interface import (
    menu_principal, 
    menu_restaurante, 
    menu_entrada_usuario, 
    menu_usuario
)
from Classes.SistemaDeDelivery import SistemaDelivery
from Classes.ItemCardapio import ItemCardapio
from Classes.Pedido import Pedido
from Classes.Observer import (NotificacaoRestaurante, 
                            NotificacaoUsuario, 
                            PedidoNotifier)

def menu():
    sistema = SistemaDelivery.get_instancia()

    while True:
        menu_principal()
        opcao = input()
        if opcao == "1":
            while True:
                menu_restaurante()
                op = input()
                if op == "1":
                    nome = input("Nome: ")
                    categoria = input("Categoria: ")
                    sistema.cadastrar_restaurante(nome, categoria)
                elif op == "2":
                    sistema.listar_restaurantes()
                elif op == "3":
                    nome_rest = input("Restaurante: ").strip().lower()
                    rest = sistema.buscar_restaurante(nome_rest)
                    if not rest:
                        print("Restaurante não encontrado.\n")
                        continue
                    item = input("Nome do item: ")
                    try:
                        preco = float(input("Preço: "))
                        rest.adicionar_item(ItemCardapio(item, preco))
                    except ValueError:
                        print("Preço inválido.\n")
                elif op == "4":
                    nome_rest = input("Restaurante: ").strip().lower()
                    rest = sistema.buscar_restaurante(nome_rest)
                    if rest:
                        rest.exibir_cardapio()
                    else:
                        print("Restaurante não encontrado.\n")
                elif op == "5":
                    nome = input("Nome do restaurante: ")
                    sistema.remover_restaurante(nome)
                elif op == "6":
                    nome_rest = input("Restaurante: ").strip().lower()
                    rest = sistema.buscar_restaurante(nome_rest)
                    if not rest:
                        print("Restaurante não encontrado.\n")
                        continue
                    item = input("Nome do item: ").strip()
                    rest.remover_item(item)
                elif op == "7":
                    nome = input("Restaurante: ").strip().lower()
                    rest = sistema.buscar_restaurante(nome)
                    if rest:
                        rest.detalhes()
                    else:
                        print("Restaurante não encontrado.\n")
                elif op == "8":
                    categoria = input("Categoria: ")
                    sistema.filtrar_por_categoria(categoria)
                elif op == "9":
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida.\n")
            
        elif opcao == "2":
            menu_entrada_usuario()
            op = input()
            if op == "1":
                sistema.cadastrar_usuario()
            else:
                user_logado = sistema.processar_login()
                if user_logado:
                    pedido_atual = None
                    while True:
                        menu_usuario()
                        op = input()
                        if op == "1":
                            sistema.listar_restaurantes()
                            nome_rest = input("\nDe qual restaurante você vai fazer o pedido? ").strip().lower()
                            rest = sistema.buscar_restaurante(nome_rest)
                            if rest:
                                rest.exibir_cardapio()
                                prato = input("\nQual prato você vai adicionar ao carrinho? ")
                                item = next((i for i in rest.cardapio if i.nome.lower() == prato.lower()), None)
                                if item:
                                    user_logado.adicionar_item(item)
                                    if pedido_atual is None or pedido_atual.restaurante != rest:
                                        pedido_atual = Pedido(rest)
                                        # REGISTRA OS OBSERVER NO PUBLISHER
                                        pedido_atual.notifier.adicionar_subscriber(NotificacaoUsuario())
                                        pedido_atual.notifier.adicionar_subscriber(NotificacaoRestaurante())
                                    pedido_atual.adicionar_item(item)
                                else:
                                    print("Prato não encontrado no cardápio.\n")
                            else:
                                print("Restaurante não encontrado.\n")
                            
                                    
                        elif op == "2":
                            user_logado.exibir_carrinho()

                        elif op == "3":
                            user_logado.exibir_carrinho()
                            prato = input("\nQual prato você vai remover do carrinho? ")
                            if pedido_atual:
                                item = next((i for i in pedido_atual.itens if i.nome.lower() == prato.lower()), None)
                                if item:
                                    user_logado.remover_item(item)
                                    pedido_atual.remover_item(item)
                                else:
                                    print("Prato não encontrado no carrinho.\n")
                            else:
                                print("Não há itens no carrinho.\n")

                        elif op == "4":
                            if pedido_atual and pedido_atual.itens:
                                sistema.fazer_pedido(pedido_atual)
                                pedido_atual.avancar_estado()
                                pedido_atual.avancar_estado()
                                user_logado.carrinho.clear()
                                pedido_atual = None
                            else:
                                print("Não há itens no pedido.\n")

                        elif op == "5":
                            user_logado.avaliar_prato()

                        elif op == "6":
                            print("Saindo...")
                            break

                        else:
                            print("Opção inválida.\n")
                else:
                    print("Login falhou.\n")
                    continue
        else:
            break        


if __name__ == "__main__":
    menu()