class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    def __str__(self):
        return f"{self._nome} - R$ {self._preco:.2f}"
