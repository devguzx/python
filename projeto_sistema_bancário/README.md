# 🏦 Sistema Bancário Simples

## 📄 Descrição

Este projeto foi desenvolvido em **Python**, com o objetivo de simular um **sistema bancário básico**, capaz de realizar operações comuns como **depósitos, saques, extrato, cadastro de usuários, criação de contas correntes e listagem de contas e usuários**.

O código foi desenvolvido inicialmente de forma procedural e posteriormente refatorado utilizando funções, tornando-o mais organizado, legível e fácil de manter.

---

##  Funcionalidades

- ✅ **Depósito de valores**
  - Permite realizar depósitos de valores positivos.

- ✅ **Saque de valores**
  - Limite de **R$ 500,00 por saque**.
  - Máximo de **3 saques diários** por conta.
  - Não permite saque superior ao saldo disponível.

- ✅ **Consulta de extrato**
  - Lista todos os depósitos e saques realizados.
  - Exibe o saldo atual da conta.

- ✅ **Cadastro de Usuários**
  - Armazena informações como: nome, CPF (chave única), data de nascimento e endereço.
  - Garante que não haja duplicidade de usuários por CPF.

- ✅ **Criação de Contas Correntes**
  - Cada conta possui uma agência fixa (padrão `0001`) e um número único.
  - A conta é associada a um CPF de um usuário previamente cadastrado.

- ✅ **Listagem de Usuários**
  - Exibe todos os usuários cadastrados no sistema.

- ✅ **Listagem de Contas**
  - Mostra as contas criadas, informando agência, número da conta e dados do titular.

- ✅ **Encerramento da operação**
  - Opção para encerrar o sistema de forma segura.

---

##  Tecnologias Utilizadas

-  **Python 3** (linguagem principal)

---

##  Regras de Negócio

- Cada CPF pode ter **uma ou mais contas correntes** associadas.
- Um usuário deve estar previamente cadastrado para criar uma conta.
- O **CPF é a chave única** de identificação dos usuários.
- As movimentações financeiras (depósitos e saques) são registradas e exibidas no extrato.
- As operações são **temporárias**, sem persistência de dados em banco de dados ou arquivos externos. Ao encerrar o programa, os dados são perdidos.

---

##  Observações

- Este projeto foi desenvolvido com foco no aprimoramento das seguintes habilidades:
  - 🧠 **Lógica de Programação**
  - 🔁 **Controle de Fluxo**
  - 🏗️ **Estruturação com Funções**
  - 🔍 **Validação de Dados e Regras de Negócio**
- É uma simulação educacional, sem persistência de dados.

---


