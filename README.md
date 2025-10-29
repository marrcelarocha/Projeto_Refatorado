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

---

## 📂 Estrutura do Código

- `Classes/` → pasta contendo todas as classes:
  - `Usuario.py` → representa o usuário  
  - `UsuarioBuilder.py` → construtor passo a passo do usuário  
  - `UsuarioDiretor.py` → diretor para construir usuários completos  
  - `SistemaDeDelivery.py` → gerencia restaurantes, pedidos e usuários  
  - `Restaurante.py` → gerencia nome, categoria e lista de itens  
  - `ItemCardapio.py` → representa um item do cardápio  
  - `Pedido.py` → adiciona itens e calcula o total  
  - `Pagamento*.py` → implementações de pagamento (Pix e Cartão)
  - `State.py` → implementa passo a passo o padrão comportamental state
  - `Observer.py` → implementa passo a passo o padrão comportamental observer
  - `Strategy.py` → implementa passo a passo o padrão comportamental strategy
  - `Decorator.py` → Implementa o padrão Decorator (comportamentos extras em pedidos)
  - `DeliveryFacade.py` → Implementa o padrão Facade (interface simplificada para o sistema)
  - `FactoryMethod.py` → Criação de objetos de pagamento (Pix, Cartão, etc.)
  - `ItemCombo.py` → Implementa o padrão Composite (combina múltiplos itens em um combo)
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



