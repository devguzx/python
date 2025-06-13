#A indentação em python é muito importante, pois a partir ela que o interpretador consegue determinar onde o bloco de comando inicia e termina.

def sacar(valor):
    saldo=500
    if saldo>=valor:
        saldo-=valor
        print(f"Sacou {valor} reias. Saldo atual = {saldo}")
    else:
        print("Saldo insuficiente!")
sacar(600)