
# Interface state
class EstadoPedido:
    def avancar(self, pedido):
        raise NotImplementedError("Cada estado deve implementar o método avancar.")

#
class AguardandoPagamento(EstadoPedido):
    def avancar(self, pedido):
        pedido.estado = Preparando()
        pedido.notifier.notificar("Pagamento confirmado! Pedido está sendo preparado.")  

class Preparando(EstadoPedido):
    def avancar(self, pedido):
        pedido.estado = Entregue()
        pedido.notifier.notificar("Pedido entregue.")


class Entregue(EstadoPedido):
    def avancar(self, pedido):
        pedido.notifier.notificar("Pedido já foi entregue.")