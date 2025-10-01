from Restaurante import Restaurante
from Usuario import Usuario
from Pedido import Pedido
from FactoryMethod import (Pagamento, PagamentoFactory, PagamentoCartao, PagamentoCartaoFactory, PagamentoPix, PagamentoPixFactory)
from UsuarioBuilder import UsuarioBuilder
from UsuarioDiretor import UsuarioDiretor

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
        usuario_final = diretor.construir_usuario_completo(
        nome, login, senha, endereco, telefone
        )

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
        total = pedido.resumo()
        metodo = input("Escolha método de pagamento (pix/cartao): ").strip().lower()

        # ⭐⭐ POLIMORFISMO CORRETO - Cria objeto primeiro, depois chama processar()
        pagamento = None
        
        if metodo == "pix":
            chave = input("Digite sua chave PIX: ").strip()
            fabrica = PagamentoPixFactory(chave)
        elif metodo == "cartao":
            numero = input("Número do cartão: ").strip()
            titular = input("Titular do cartão: ").strip()
            cvv = input("CVV: ").strip()
            fabrica = PagamentoCartaoFactory(numero, titular, cvv)
        else:
            print("Método inválido, pedido cancelado.\n")
            return
        
        pagamento = fabrica.criar_pagamento()        
        
        pagamento.processar(total)
