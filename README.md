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

## 🚀 Próximos passos (Ideias de Evolução)
Como este projeto é a primeira versão via terminal, as próximas atualizações planejadas para evoluir o sistema incluem:

* **Interface Gráfica (GUI):** Sair da tela de texto e criar uma janela visual interativa com campos de digitação e botões (utilizando Tkinter).
* **Banco de Dados Local:** Criar um salvamento automático (utilizando SQLite) para guardar o histórico de fechamentos diários e permitir consultas de dias anteriores.
* **Geração de Executável (.exe):** Empacotar o sistema para que o usuário final possa rodar o programa com apenas dois cliques na Área de Trabalho, sem precisar instalar o Python.
* **Mais Formas de Pagamento:** Adicionar suporte para múltiplos cartões e vouchers (Alelo, TicketLog, Premmia, etc.).


# 💻 Sistema de Fechamento de Caixa v2.0 (Com Interface Gráfica)

Esta é a evolução direta do meu primeiro sistema de automação de caixa. O projeto saiu do terminal de linha de comando e agora possui uma interface visual completa, banco de dados local para persistência de informações e exportação de relatórios profissionais!

<img width="398" height="922" alt="fechamento01" src="https://github.com/user-attachments/assets/40ced728-b32d-4f6d-87a2-61d025b0e0cc" />


## ✨ O que há de novo nesta versão? (Melhorias Implementadas)
A versão 2.0 foi desenvolvida focando na experiência do usuário final (operador de caixa) e nas necessidades administrativas do dono do negócio. As principais evoluções incluem:

* **Interface Gráfica (GUI):** O sistema agora possui uma janela amigável, intuitiva e interativa, eliminando totalmente a necessidade de uso do terminal.
* **Múltiplas Formas de Pagamento:** Inclusão de um portfólio completo de recebimentos, com mais de 15 novos campos (Cartões de Crédito/Débito, Pix, TicketLog, Alelo, Nutricash, Quinzenal, Semanal, etc.).
* **Banco de Dados Local:** Implementação de um banco de dados para salvar, de forma silenciosa e automática, todos os fechamentos realizados.
* **Tela de Auditoria (Histórico):** Um painel secundário dedicado para visualizar os resultados dos dias anteriores.
* **Exportação para Excel:** Com apenas um clique, o sistema compila todo o histórico do banco de dados e gera uma planilha `.csv` pronta para envio à contabilidade.
* **Geração de Comprovante Físico:** Criação automática de um recibo em formato `.txt` (layout de cupom) a cada fechamento concluído.

<img width="794" height="624" alt="fechamento02" src="https://github.com/user-attachments/assets/4a72175f-3f1b-4725-970b-492835358e68" />


## 🛠️ Tecnologias e Bibliotecas Utilizadas
Este projeto foi desenvolvido inteiramente em Python, focando no uso de bibliotecas nativas para garantir um executável leve e rápido.

* **Python 3:** Linguagem base de todo o ecossistema.
* **Tkinter:** Criação da Interface Gráfica (GUI), botões, inputs e tabelas (Treeview).
* **SQLite3:** Construção e gerenciamento do banco de dados relacional sem necessidade de servidores externos.
* **CSV & Datetime:** Manipulação nativa de datas e exportação estruturada de arquivos de planilha.
* **PyInstaller:** Empacotamento de todos os scripts e bibliotecas para a geração do arquivo `.exe`, permitindo que o cliente rode o programa com dois cliques sem precisar ter o Python instalado.

## 🚀 Em Desenvolvimento: Versão PRO (Sneak Peek)

O aprendizado e a evolução do projeto não param! Já estou desenvolvendo a **Versão 3.0 (PRO)** do sistema, que trará uma reformulação visual completa e novos recursos voltados para a gestão e segurança do negócio.

**O que está sendo construído para a próxima grande atualização:**

* **Sistema de Autenticação (Login):** Controle de acesso rigoroso com usuário e senha, garantindo a segurança e o rastreio de quem realizou os fechamentos.
* **Controle de Níveis de Acesso:** O sistema identificará se o usuário logado é um "Administrador" (com acesso total) ou um "Operador" (com acesso restrito apenas ao fechamento diário).
* **Novo Design Premium (Dark Mode):** Uma interface gráfica totalmente redesenhada, muito mais moderna e agradável para uso prolongado.
* **Navegação por Menu Lateral:** Estruturação em abas, preparando o terreno para novos módulos.
* **Novos Módulos Planejados:** Telas futuras para gestão de "Usuários", "Configurações" e um "Dashboard" com gráficos de desempenho do caixa.
