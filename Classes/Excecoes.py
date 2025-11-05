# Excecoes.py

# Classe base para todas as exceções do sistema
class DeliveryError(Exception):
    def __init__(self, message):
        # chama o construtor da classe mae (Exception) para manter o comportamento padrão 
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message}"


# Singleton
class SingletonReinitializationError(DeliveryError):
    def __init__(self, nome_classe):
        super().__init__(f"Singleton '{nome_classe}' não pode ser reinicializado.")


# Builder
class BuilderIncompleteError(DeliveryError):
    def __init__(self, missing_fields):
        campos = ", ".join(missing_fields)
        super().__init__(f"Builder incompleto. Campos ausentes: {campos}")


# Factory
class FactoryResolutionError(DeliveryError):
    def __init__(self, family, key, registered):
        super().__init__(
            f"Factory '{family}' não encontrou implementação para '{key}'. "
            f"Implementações disponíveis: {registered}"
        )


# Pagamento
class PaymentError(DeliveryError):
    def __init__(self, metodo, motivo):
        super().__init__(f"Falha no pagamento via {metodo}: {motivo}")


# Validação genérica
class ValidationError(DeliveryError):
    def __init__(self, message):
        super().__init__(f"Erro de validação: {message}")
