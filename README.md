# 📊 Sistema de Fechamento de Caixa (Versão Terminal)

Este é um programa simples e direto desenvolvido em Python para automatizar o cálculo e a conferência do fechamento de caixa diário de pequenos comércios.

## 🎯 O que o código faz?
Ele substitui a calculadora e o papel, cruzando o valor que o sistema de vendas diz que deveria ter com o valor físico real que o operador de caixa tem em mãos.

**O passo a passo do programa:**
* Solicita o valor total de vendas registrado no sistema da loja.
* Pede a entrada individual dos valores recebidos por cada forma de pagamento (Dinheiro, Visa, Mastercard e Pix).
* Soma automaticamente todas as entradas físicas.
* Compara o valor físico com o valor do sistema.
* Exibe um **Resumo do Caixa**, informando o status final:
  - **Caixa Batido:** Quando não falta nem sobra um centavo.
  - **Sobra de Caixa:** Quando há dinheiro a mais do que o esperado.
  - **Quebra de Caixa:** Quando está faltando dinheiro.

## 🚀 Como executar o projeto
1. Certifique-se de ter o Python instalado no seu computador.
2. Baixe o arquivo do código.
3. Abra o terminal e execute o comando:
`python nome_do_arquivo.py` (substitua pelo nome real do arquivo).

## 🛠️ Tecnologias Utilizadas
* Python
* Tratamento de exceções (`try/except`) para evitar erros de digitação (como digitar letras no lugar de números).
