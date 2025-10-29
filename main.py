from Interface import (
    menu_principal,
    menu_restaurante,
    menu_entrada_usuario,
    menu_usuario
)
from Classes.DeliveryFacade import DeliveryFacade
from Classes.ItemCardapio import ItemCardapio
from Classes.ItemComponente import ItemComponente

def menu():
    facade = DeliveryFacade()

    while True:
        menu_principal()
        opcao = input()

        # ===================== MENU RESTAURANTE =====================
        if opcao == "1":
            while True:
                menu_restaurante()
                op = input()

                if op == "1":
                    nome = input("Nome: ")
                    categoria = input("Categoria: ")
                    facade.cadastrar_restaurante(nome, categoria)

                elif op == "2":
                    facade.listar_restaurantes()

                elif op == "3":
                    nome_rest = input("Restaurante: ").strip().lower()
                    rest = facade.buscar_restaurante(nome_rest)
                    if not rest:
                        print("Restaurante não encontrado.\n")
                        continue

                    print("\nO que deseja adicionar?")
                    print("1 - Adicionar item simples")
                    print("2 - Criar combo")
                    tipo = input("Escolha: ")

                    if tipo == "1":
                        rest.criar_item_simples()
                    elif tipo == "2":
                        rest.criar_combo()
                    else:
                        print("Opção inválida.\n")

                elif op == "4":
                    nome_rest = input("Restaurante: ").strip().lower()
                    facade.exibir_cardapio(nome_rest)

                elif op == "5":
                    nome = input("Nome do restaurante: ")
                    facade.sistema.remover_restaurante(nome)

                elif op == "6":
                    nome_rest = input("Restaurante: ").strip().lower()
                    rest = facade.buscar_restaurante(nome_rest)
                    if rest:
                        item = input("Nome do item: ").strip()
                        rest.remover_item(item)
                    else:
                        print("Restaurante não encontrado.\n")

                elif op == "7":
                    nome = input("Restaurante: ").strip().lower()
                    rest = facade.buscar_restaurante(nome)
                    if rest:
                        rest.detalhes()
                    else:
                        print("Restaurante não encontrado.\n")

                elif op == "8":
                    categoria = input("Categoria: ")
                    facade.sistema.filtrar_por_categoria(categoria)

                elif op == "9":
                    print("Saindo...")
                    break

                else:
                    print("Opção inválida.\n")

        # ===================== MENU USUÁRIO =====================
        elif opcao == "2":
            menu_entrada_usuario()
            op = input()

            if op == "1":
                facade.cadastrar_usuario()
            else:
                user_logado = facade.login()
                if user_logado:
                    pedido_atual = None
                    while True:
                        menu_usuario()
                        op = input()

                        if op == "1":
                            facade.listar_restaurantes()
                            
                            nome_rest = input("\nDe qual restaurante você vai fazer o pedido? ").strip().lower()
                            rest = facade.buscar_restaurante(nome_rest)
                            
                            if rest:
                                rest.exibir_cardapio()                                
                                prato = input("\nQual prato ou combo você vai adicionar ao carrinho? ").strip().lower()
                                item = next((i for i in rest.cardapio if i.get_nome().lower() == prato), None)
                                
                                if item:
                                    user_logado.adicionar_item(item)
                                    
                                    if pedido_atual is None or pedido_atual.restaurante != rest:
                                        pedido_atual = facade.criar_pedido(user_logado, rest)
                                    
                                    facade.adicionar_item_pedido(pedido_atual, item)
                                    
                                    print(f"{item.get_nome()} adicionado ao pedido!")
                                else:
                                    print("Item ou combo não encontrado no cardápio.\n")
                            else:
                                print("Restaurante não encontrado.\n")


                        elif op == "2":
                            user_logado.exibir_carrinho()

                        elif op == "3":
                            user_logado.exibir_carrinho()
                            prato = input("\nQual prato você vai remover do carrinho? ")
                            if pedido_atual:
                                item = next((i for i in rest.cardapio if i.get_nome().lower() == prato.lower()), None)
                                if item:
                                    user_logado.remover_item(item)
                                    facade.remover_item_pedido(pedido_atual, item)
                                else:
                                    print("Prato não encontrado no carrinho.\n")
                            else:
                                print("Não há itens no carrinho.\n")

                        elif op == "4":
                            if pedido_atual and pedido_atual.itens:
                                facade.finalizar_pedido(pedido_atual)
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
