#Operadores de Comparação: Comparar valores
#Retorna valores booleanos

saldo,saque=1000,200
print(saldo>saque) #Maior que
print(saldo<saque) #Menor que
print(saldo==saque) #Igual
print(saldo!=saque) #Diferente

#Exemplo:
try:
    idade = int(input("Digite sua idade: "))
    if idade < 0:
        print("Idade inválida.")
    elif idade >= 18:
        print("Você já está na maioridade.")
    elif 13 < idade < 18:
        print("Você é pré-adolescente.")
    else:
        print("Você é criança.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")




