#Comando while: Usado quando nao se sabe o número de vezes que o bloco de código vai ser executado .

#Exemplo: contador
cont=0
while cont<=10:
    print(cont)
    cont+=1

#Exemplo: acerte a senha
SENHA="python123"
while True:
    senha_informada=input("Digite a senha para entar no sistema:")
    if SENHA==senha_informada:
        print("Parabéns você acertou a senha!")
        break
    else:
        print("----------------")
        print("SENHA INCORRETA!")
        print("----------------")
    