from Classes.Excecoes import BuilderIncompleteError

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
        
        usuario = self.builder.get_resultado()

        # validação dos campos obrigatórios
        missing = []
        if not usuario.nome:
            missing.append("nome")
        if not usuario.login:
            missing.append("login")
        if not usuario.senha:
            missing.append("senha")
        if not usuario.endereco:
            missing.append("endereco")
        if not usuario.telefone:
            missing.append("telefone")

        if missing:
            raise BuilderIncompleteError(missing)

        return usuario