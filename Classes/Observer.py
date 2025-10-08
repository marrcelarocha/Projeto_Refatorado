# --- OBSERVER ---

# SUBSCRIBER

class Observer:
    def update(self, mensagem):
        pass

# CONCRETE SUBSCRIBERS

class NotificacaoUsuario(Observer):

    def update(self, mensagem):
        print(f"[Usuário] Notificação recebida: {mensagem}")


class NotificacaoRestaurante(Observer):

    def update(self, mensagem):
        print(f"[Restaurante] Notificação recebida: {mensagem}")


# PUBLISHER

class PedidoNotifier:
    def __init__(self):
        self._observers = []

    def adicionar_subscriber(self, obs: Observer):
        self._observers.append(obs)

    def remover_subscriber(self, obs: Observer):
        self._observers.remove(obs)

    def notificar(self, mensagem):
        for obs in self._observers:
            obs.update(mensagem)
