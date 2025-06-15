# ======== Projeto 01: Sistema Bancário Simples ========

# Variáveis principais
saldo = 0
depositos = []
saques = []

LIMITE_SAQUE = 500
LIMITE_DIARIO = 3
limite_saque_diario = 0


def menu():
    print("""
=============== SISTEMA BANCÁRIO ===============
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Sair
===============================================
""")


def depositar():
    global saldo, depositos
    deposito = float(input("Qual valor deseja depositar? "))

    if deposito <= 0:
        print("Valor inválido!")
    else:
        saldo += deposito
        depositos.append(deposito)
        print(f"Depósito de {deposito} reais realizado com sucesso!")
        print(f"Seu saldo: {saldo}")


def sacar():
    global saldo, saques, limite_saque_diario
    saque = float(input("Qual valor deseja sacar? "))

    if saque <= 0:
        print("Valor de saque inválido!")
    elif saque > saldo:
        print("Não é possível realizar o saque. Saldo insuficiente!")
    elif saque > LIMITE_SAQUE:
        print("Não é possível realizar o saque. O valor excede o limite de R$500 por saque!")
    elif limite_saque_diario >= LIMITE_DIARIO:
        print("Limite de saques diários atingido.")
    else:
        saldo -= saque
        saques.append(saque)
        limite_saque_diario += 1
        print(f"Saque de {saque} reais realizado com sucesso!")
        print(f"Seu saldo: {saldo}")


def extrato():
    print("====== EXTRATO ======")
    if not depositos:
        print("Nenhum depósito realizado.")
    else:
        for d in depositos:
            print(f"Depósito: R$ {d:.2f}")

    if not saques:
        print("Nenhum saque realizado.")
    else:
        for s in saques:
            print(f"Saque: R$ {s:.2f}")

    print(f"Saldo atual: R$ {saldo:.2f}")
    print("======================\n")


while True:
    menu()

    operacao = int(input("Digite o número da operação: "))

    if operacao == 1:
        depositar()
    elif operacao == 2:
        sacar()
    elif operacao == 3:
        extrato()
    elif operacao == 4:
        print("Até mais, volte logo.")
        break
    else:
        print("Operação inválida, por favor escolha uma operação válida.")
