# 🍽️ Otavio's Food Service

Um sistema simples de **delivery online** feito em **Python**,
utilizando POO (*Programação Orientada a Objetos*).\
Ele permite cadastrar restaurantes, adicionar itens ao cardápio, fazer
pedidos e processar pagamentos.

------------------------------------------------------------------------

## 📌 Funcionalidades

✅ **Gerenciamento de Restaurantes** - Cadastro de novos restaurantes -
Listagem de todos os restaurantes - Filtragem por categoria - Remoção de
restaurantes

✅ **Gerenciamento de Cardápio** - Adicionar itens ao cardápio de cada
restaurante - Remover itens - Visualizar o cardápio completo

✅ **Sistema de Pedidos** - Selecionar restaurante - Escolher itens do
cardápio - Gerar resumo do pedido com preço total

✅ **Pagamentos** - **PIX** (exibe chave PIX) - **Cartão de crédito**
(exibe número mascarado)

✅ **Simulação de Entrega** - Exibe mensagens de saída para entrega e
entrega concluída

OBS: Existem funcionalidades dentro de outras funcionalidades.


------------------------------------------------------------------------

## 🛠️ Tecnologias Utilizadas

-   Paradigma **POO**
-   Módulo `abc` para classes abstratas

------------------------------------------------------------------------

## 📂 Estrutura do Código

-   `ItemCardapio` → representa um item do cardápio
-   `Restaurante` → gerencia nome, categoria e lista de itens
-   `Pedido` → adiciona itens e calcula o total
-   `Pagamento` (classe abstrata) → define interface para pagamentos
-   `PagamentoPix` e `PagamentoCartao` → implementam métodos de
    pagamento
-   `SistemaDelivery` → gerencia restaurantes, pedidos e fluxo do
    sistema
-   `menu()` → interface simples no terminal para o usuário

------------------------------------------------------------------------

## ▶️ Como Executar

1.  Certifique-se de ter **Python 3** instalado:

    ``` bash
    python --version
    ```

2.  Rode o arquivo principal:

    ``` bash
    python nome_do_arquivo.py
    ```
