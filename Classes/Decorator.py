# DecoratorPedido.py
class PedidoDecorator:
    def __init__(self, pedido):
        self._pedido = pedido
        self._adicionais = []
        self._custo_adicionais = 0

    def adicionar_embalagem_premium(self):
        self._adicionais.append("Embalagem Premium")
        self._custo_adicionais += 5.0

    def adicionar_entrega_rapida(self):
        self._adicionais.append("Entrega Rápida")
        self._custo_adicionais += 6.0

    def resumo(self):
        base_total = self._pedido.resumo()  # usa o resumo original (que já aplica o desconto)
        print(f"Adicionais: {', '.join(self._adicionais) if self._adicionais else 'Nenhum'}")
        print(f"Total final com adicionais: R$ {base_total + self._custo_adicionais:.2f}")
        return base_total + self._custo_adicionais
