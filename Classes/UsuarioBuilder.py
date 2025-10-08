from Classes.Usuario import Usuario

# responsável por montar o usuário passo a passo
class UsuarioBuilder:
    def __init__(self):
        self.usuario = Usuario(nome="", 
                               login="", 
                               senha="")

    def definir_nome(self, nome):
        self.usuario.nome = nome
        return self
    
    def definir_login(self, login):
        self.usuario.login = login
        return self
    
    def definir_senha(self, senha):
        self.usuario.senha = senha
        return self
    
    def definir_endereco(self, endereco):
        self.usuario.endereco = endereco
        return self

    def definir_telefone(self, telefone):
        self.usuario.telefone = telefone
        return self

    def definir_historico_pedidos(self, pedido):
        self.usuario.historico_pedidos.append(pedido)
        return self

    def get_resultado(self):
        return self.usuario