# Sistema Bancário Simples

## Descrição

Este é um projeto desenvolvido em Python com o objetivo de simular um sistema bancário básico. O programa permite ao usuário realizar operações como **depósito**, **saque** e **consultar extrato**, com regras simples de negócio, como limite de saque por operação e por dia.

O projeto foi desenvolvido inicialmente de forma procedural e posteriormente refatorado utilizando funções, visando melhorar a organização, a legibilidade e a manutenção do código.

---

## Funcionalidades

- ✅ Depósito de valores (apenas valores positivos).
- ✅ Saque de valores com as seguintes restrições:
  - Limite de **R$ 500,00** por saque.
  - Máximo de **3 saques diários**.
  - Não permite saque superior ao saldo disponível.
- ✅ Consulta de extrato:
  - Lista todos os depósitos e saques realizados.
  - Exibe o saldo atual.
- ✅ Encerramento da operação (**Sair do sistema**).

---

## Tecnologias Utilizadas

- **Python 3**

## Observações

- Este projeto foi desenvolvido com foco em prática de lógica de programação, controle de fluxo, uso de funções e organização de código.
- As operações não persistem os dados. Ao encerrar o programa, todos os dados são perdidos, pois não há integração com banco de dados ou arquivos externos.
