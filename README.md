# 🍽️ Otavio's Food Service

Um sistema simples de **delivery online** feito em **Python**, utilizando POO (*Programação Orientada a Objetos*).  
Permite cadastrar restaurantes, adicionar itens ao cardápio, criar usuários, fazer pedidos e processar pagamentos, utilizando padrões de projeto como **Builder**, **Singleton** , **Factory Method**, **Observer** e **State**

------------------------------------------------------------------------

## 📌 Funcionalidades

✅ **Gerenciamento de Restaurantes**  
- Cadastro de novos restaurantes  
- Listagem de todos os restaurantes  
- Filtragem por categoria  
- Remoção de restaurantes  

✅ **Gerenciamento de Cardápio**  
- Adicionar itens ao cardápio de cada restaurante  
- Remover itens  
- Visualizar cardápio completo  

✅ **Gerenciamento de Usuários**  
- Cadastro de usuários utilizando **Builder**  
- Login e logout  
- Consultar detalhes do perfil e histórico de pedidos  

✅ **Sistema de Pedidos**  
- Selecionar restaurante  
- Escolher itens do cardápio  
- Adicionar/remover itens do carrinho  
- Gerar resumo do pedido com preço total  

✅ **Pagamentos**  
- **PIX** (exibe chave PIX)  
- **Cartão de crédito** (exibe número mascarado)  
- Implementado com **Factory Method**  

✅ **Simulação de Entrega**  
- Exibe mensagens de saída para entrega e entrega concluída  

---

## 🛠️ Tecnologias Utilizadas

- Paradigma **POO** (Programação Orientada a Objetos)  
- Módulo `abc` para classes abstratas  
- Padrões de projeto criacionais: **Builder**, **Singleton**, **Factory Method**
- Padrões de projeto comportamentais: **Observer**, **State**

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



