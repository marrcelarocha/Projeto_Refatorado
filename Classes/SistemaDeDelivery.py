from Classes.Restaurante import Restaurante
from Classes.Pedido import Pedido
from Classes.FactoryMethod import (Pagamento, PagamentoFactory, PagamentoCartao, PagamentoCartaoFactory, PagamentoPix, PagamentoPixFactory)
from Classes.UsuarioBuilder import UsuarioBuilder
from Classes.UsuarioDiretor import UsuarioDiretor
from Classes.Decorator import PedidoDecorator
from Classes.Excecoes import (
    BuilderIncompleteError,
    FactoryResolutionError,
    ValidationError,
)

usuarios_registrados = {}
usuario_logado = None

class SistemaDelivery:
    #campo estátivo privado
    __instancia = None

    def __init__(self):
        if SistemaDelivery.__instancia is not None:
            raise Exception("Use get_instancia() para acessar o sistema.")
        self.restaurantes = {}
        self.usuarios = {}

    #inicialização preguiçosa   
    @staticmethod
    def get_instancia():
        if SistemaDelivery.__instancia is None:
            SistemaDelivery.__instancia = SistemaDelivery()
        return SistemaDelivery.__instancia

    def cadastrar_restaurante(self, nome, categoria):
        nome = nome.lower().strip()
        if nome in self.restaurantes:
            print("Já existe um restaurante com esse nome!\n")
            return
        self.restaurantes[nome] = Restaurante(nome, categoria)
        print(f"{nome.capitalize()} cadastrado com sucesso!\n")

    def cadastrar_usuario(self):
        # cria o builder
        builder = UsuarioBuilder()

        # cria o diretor e passa o builder
        diretor = UsuarioDiretor(builder)

        nome = input("Nome: ").strip()
        login = input("Login: ").strip()
        senha = input("Senha: ").strip()
        endereco = input("Endereço: ").strip()
        telefone = input("Telefone: ").strip()

        # diretor constrói usuário completo
        try:
            usuario_final = diretor.construir_usuario_completo(nome, login, senha, endereco, telefone)
        except BuilderIncompleteError as e:
            print(f"\n[ERRO] {e}\n")
            return
        
        if login in usuarios_registrados:
            print("Este login já existe. Tente outro.")
        else:
            usuarios_registrados[login] = usuario_final
            print(f"Usuário {usuario_final.nome} cadastrado com sucesso!")

    def processar_login(self):
        global usuario_logado
        login = input("Login: ")
        senha = input("Senha: ")
        
        if login in usuarios_registrados and usuarios_registrados[login].senha == senha:
            usuario_logado = usuarios_registrados[login]
            print(f"Login bem-sucedido! Bem-vindo(a), {usuario_logado.nome}!")
            return usuario_logado
        else:
            print("Login ou senha incorreta.")
            return None

    def listar_restaurantes(self):
        if not self.restaurantes:
            print("Nenhum restaurante cadastrado.\n")
            return
        print("Restaurantes cadastrados:")
        for r in self.restaurantes.values():
            print(f"- {r.nome.capitalize()} (Categoria: {r.categoria})")
        print()

    def buscar_restaurante(self, nome):
        return self.restaurantes.get(nome.lower())

    def remover_restaurante(self, nome):
        if nome.lower() in self.restaurantes:
            del self.restaurantes[nome.lower()]
            print(f"Restaurante '{nome}' removido.\n")
        else:
            print("Restaurante não encontrado.\n")

    def filtrar_por_categoria(self, categoria):
        encontrados = [r for r in self.restaurantes.values() if r.categoria.lower() == categoria.lower()]
        if not encontrados:
            print("Nenhum restaurante encontrado.\n")
            return
        print(f"Restaurantes da categoria {categoria.capitalize()}:")
        for r in encontrados:
            print(f"- {r.nome.capitalize()}")
        print()

    def simular_entrega(self, restaurante):
        print(f"Pedido do restaurante '{restaurante.nome}' saiu para entrega.")
        print("Pedido entregue com sucesso!\n")

    def fazer_pedido(self, pedido: Pedido):

        decorado = PedidoDecorator(pedido)

        print("Deseja adicionar opcionais?")
        print("1 - Embalagem Premium (+R$5.00)")
        print("2 - Entrega Rápida (+R$6.00)")
        print("3 - Ambos")
        print("4 - Nenhum")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            decorado.adicionar_embalagem_premium()
        elif opcao == "2":
            decorado.adicionar_entrega_rapida()
        elif opcao == "3":
            decorado.adicionar_embalagem_premium()
            decorado.adicionar_entrega_rapida()

        total_final = decorado.resumo()

        metodo = input("Escolha método de pagamento (pix/cartao): ").strip().lower()

        # ⭐⭐ POLIMORFISMO CORRETO - Cria objeto primeiro, depois chama processar()
        pagamento = None
        
        try:
            if metodo == "pix":
                chave = input("Digite sua chave PIX: ").strip()
                if not chave:
                    raise ValidationError("Chave PIX não pode ser vazia.")
                fabrica = PagamentoPixFactory(chave)
            
            elif metodo == "cartao":
                numero  = input("Número do cartão: ").strip()
                titular = input("Titular do cartão: ").strip()
                cvv     = input("CVV: ").strip()
                # validações básicas
                if not (numero and titular and cvv):
                    raise ValidationError("Número, titular e CVV são obrigatórios.")
                if not numero.isdigit():
                    raise ValidationError("Número do cartão deve conter apenas dígitos.")
                if not cvv.isdigit() or len(cvv) not in (3, 4):
                    raise ValidationError("CVV deve ser numérico (3 ou 4 dígitos).")
                fabrica = PagamentoCartaoFactory(numero, titular, cvv)
            
            else:
                raise FactoryResolutionError("metodo_pagamento", metodo, registered=["pix", "cartao"])
                
        except FactoryResolutionError as e:
            print(f"[ERRO] Método de pagamento inválido: {e}")
            raise
        
        except ValidationError as e:
            print(f"[ERRO] {e}")
            raise

        except Exception as e:
            # Erros inesperados
            print(f"[ERRO INESPERADO] {e}")
            raise

        else:
            pagamento = fabrica.criar_pagamento()        
            pagamento.processar(total_final)
