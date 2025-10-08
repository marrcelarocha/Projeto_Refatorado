# responsável por usar o builder na ordem correta
class UsuarioDiretor:
    def __init__(self, builder):
        self.builder = builder

    def construir_usuario_completo(self, nome, login, senha, endereco, telefone):
        self.builder.definir_nome(nome)
        self.builder.definir_login(login)
        self.builder.definir_senha(senha)
        self.builder.definir_endereco(endereco)
        self.builder.definir_telefone(telefone)
        return self.builder.get_resultado()
