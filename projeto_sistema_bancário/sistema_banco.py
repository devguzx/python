#Projeto 01: Sistema Bancário Simples

#Inicialização das variáveis
saldo=0
depositos=[]
saques=[]
LIMITE_SAQUE=500
LIMITE_DIARIO=3
limite_saque_diario=0

#Entrada do sistema bancário
while True:
    print("""===============Sistema Bancário===============
          1-Depositar
          2-Saque
          3-Extrato
          4-Sair
    """)
    operacao_bancaria=int(input("Digite o número da operação que vc deseja realizar: "))
    
    if operacao_bancaria==1:
        deposito=float(input("Qual valor deseja depositar? "))

        if deposito<=0:
            print("Valor Inválido!")
        else:
            print(f"Deposito de {deposito} reais realizado com sucesso!")
            depositos.append(deposito)
            saldo+=deposito
            print(f"Seu saldo: {saldo}")

    elif operacao_bancaria==2:
        saque=float(input("Qual valor vc deseja sacar? "))

        if  saque>saldo:
            print("Nao é possivel realizar o saque. Saldo insuficiente!")
        elif saque>LIMITE_SAQUE:
            print("Não é possível realizar o saque. O valor excede o limite de R$500 por saque!")
        elif limite_saque_diario>=LIMITE_DIARIO:
            print("Limite de saques diarios atingidos.")
        elif saque <=0:
            print("Valor de saque inválido!")
        else:
            print(f"Saque de {saque} reais realizado com sucesso!")
            saldo-=saque
            limite_saque_diario+=1
            saques.append(saque)

    elif operacao_bancaria==3:
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
        print("======================")

    elif operacao_bancaria==4:
        print("Ate mais, volte logo.")
        break
    else:
        print("Operação Invalida, por favor respeite as operações do sistema.")
        


    