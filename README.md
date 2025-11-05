# 🍽️ Otavio's Food Service

Um sistema simples de **delivery online** feito em **Python**, utilizando POO (*Programação Orientada a Objetos*).  
Permite cadastrar restaurantes, adicionar itens ao cardápio, criar usuários, fazer pedidos e processar pagamentos, utilizando padrões de projeto como **Builder**, **Singleton** , **Factory Method**, **Observer**, **State**, **Strategy**, **Decorator**, **Facade** e **Compositer**


------------------------------------------------------------------------

## 📌 Funcionalidades

✅ **Gerenciamento de Restaurantes**  
- Cadastro e listagem de restaurantes  
- Filtragem por categoria  
- Remoção de restaurantes  

✅ **Gerenciamento de Cardápio**  
- Adicionar e remover itens  
- Visualizar o cardápio completo  
- Criação de **combos de produtos** com o padrão **Composite**

✅ **Gerenciamento de Usuários**  
- Cadastro de usuários com o padrão **Builder**  
- Login e logout  
- Exibição de perfil e histórico de pedidos  

✅ **Sistema de Pedidos**  
- Selecionar restaurante  
- Adicionar itens ou **combos** ao carrinho  
- Remover itens  
- Gerar resumo com aplicação dinâmica de descontos (Strategy)  

✅ **Pagamentos**  
- Pagamento via **PIX** ou **Cartão de Crédito**  
- Implementado com o padrão **Factory Method**

✅ **Simulação de Entrega**  
- Transição de estados do pedido (aguardando pagamento → preparando → entregue)  
- Implementada com o padrão **State**  
- Envio automático de notificações usando **Observer**

✅ **Interface Simplificada**  
- O padrão **Facade** centraliza o acesso às principais operações do sistema (usuários, pedidos, restaurantes etc.)  
- Facilita o uso da aplicação a partir do arquivo `main.py`

---

## 🛠️ Tecnologias Utilizadas

- Paradigma **POO** (Programação Orientada a Objetos)  
- Módulo `abc` para classes abstratas  
- Padrões de projeto criacionais: **Builder**, **Singleton**, **Factory Method**
- Padrões de projeto comportamentais: **Observer**, **State**, **Strategy**
- Padrões de projeto estruturais: **Decorator**, **Facade**, **Compositer**

### ⚙️ Design Patterns e onde se encontram

- `Padrões criacionais` 
  - `Builder`   
    - `Usuario.py`
    - `UsuarioBuilder.py`
    - `UsuarioDiretor.py`
  - `Singleton`   
    - `SistemaDelivery.py`
  - `Factory Method`   
    - `FactoryMethod.py`
- `Padrões comportamentais` 
  - `Observer`   
    - `Observer.py`
  - `State`   
    - `State.py`
  - `Strategy`   
    - `Strategy.py`
- `Padrões estruturais` 
  - `Decorator`   
    - `Decorator.py`
  - `Facade`   
    - `DeliveryFacade.py`
  - `Compositer`   
    - `ItemCombo.py` 
    - `ItemComponente.py` 
    - `ItemSimples.py` 
---

## 🧩 Tratamento de Exceções no Sistema de Pagamentos

O sistema possui um módulo dedicado chamado `Excecoes.py`, que centraliza todas as exceções personalizadas utilizadas nas demais classes.  
Essas exceções são projetadas para lidar com diferentes situações de erro dentro do fluxo do sistema de delivery.
No sistema foi utilizado a exceção do tipo `Try/Except/Else`.

### ⚙️ Hierarquia das Exceções
Todas as exceções herdam de DeliveryError, que por sua vez herda da classe nativa Exception do Python.

- `Exception` 
  - `DeliveryError`   
    - `BuilderIncompleteError` 
    - `FactoryResolutionError` 
    - `PaymentError` 
    - `ValidationError` 

### 🧠 Descrição das Exceções

- `DeliveryError`
  - **Classe base** para todas as exceções do sistema.
  - Armazena uma mensagem de erro personalizada e sobrescreve o método __str__ para exibição clara no terminal.
- `BuilderIncompleteError`
  - **Origem:** Método de cadastro de usuários na classe SistemaDelivery.
  - **Quando ocorre:** Quando o UsuarioBuilder não recebe todos os campos necessários para criar um usuário completo.
- `FactoryResolutionError`
  - **Origem:** Método de fazer pedido na classe SistemaDelivery.
  - **Quando ocorre:** Quando o usuário escolhe um método de pagamento inválido (diferente de "pix" ou "cartao").
- `PaymentError`
  - **Origem:** Módulos de pagamento (PagamentoPix, PagamentoCartao).
  - **Quando ocorre:** Quando há falha ao processar o pagamento.
- `ValidationError`
  - **Origem:** Validação de entrada de dados (como número do cartão, CVV, chave PIX).
  - **Quando ocorre:** Quando um dado informado pelo usuário não atende às regras de formato ou obrigatoriedade.
---

## 📂 Estrutura do Código

- `Classes/` → pasta contendo todas as classes:
  - `Usuario.py` → representa o usuário  
  - `UsuarioBuilder.py` → construtor passo a passo do usuário; Implementa o padrão **Builder** .
  - `UsuarioDiretor.py` → diretor para construir usuários completos  
  - `SistemaDeDelivery.py` → gerencia restaurantes, pedidos e usuários. **Singleton** implementado, garantindo que uma única instância seja criada.
  - `Restaurante.py` → gerencia nome, categoria e lista de itens  
  - `ItemCardapio.py` → representa um item do cardápio  
  - `Pedido.py` → adiciona itens e calcula o total  
  - `Pagamento*.py` → implementações de pagamento (Pix e Cartão)
  - `State.py` → implementa passo a passo o padrão comportamental **state**
  - `Observer.py` → implementa passo a passo o padrão comportamental **observer**
  - `Strategy.py` → implementa passo a passo o padrão comportamental **strategy**
  - `Decorator.py` → Implementa o padrão **Decorator** (comportamentos extras em pedidos)
  - `DeliveryFacade.py` → Implementa o padrão **Facade** (interface simplificada para o sistema)
  - `FactoryMethod.py` → Criação de objetos de pagamento (Pix, Cartão, etc.); Implementa o padrão **FactoryMethod**
  - `ItemCombo.py` → Implementa o padrão **Composite** (combina múltiplos itens em um combo)
  - `ItemComponente.py` → Interface abstrata do Composite
  - `ItemSimples.py` → Representa itens individuais do cardápio
- `main.py` → arquivo principal que executa o sistema  
- `interface.py` → funções de menu e interação com o usuário  

---

## ▶️ Como Executar

1. Certifique-se de ter **Python 3** instalado:

```bash
python --version
```

2. Execute o arquivo principal:

```bash
python main.py
```

3. Siga os menus no terminal para:

- Cadastrar restaurantes e usuários
- Adicionar itens ao cardápio
- Fazer pedidos e processar pagamentos
- Consultar carrinho e histórico

---

## ⚙️ Observações

- Todos os arquivos de classes estão dentro da pasta `Classes/`.
- `main.py` deve ser executado **a partir da raiz do projeto** para que os imports funcionem corretamente.
- O cadastro de usuários utiliza **Builder**, permitindo adicionar informações passo a passo.
- O sistema garante **uma única instância** de `SistemaDelivery` com o padrão **Singleton**.



