#Variáveis: valores que podem sofrer alterações no decorrer da execução do programa.

#Exemplo - Saque no banco
saldo=1000
valor_sacado=int(input("Qual valor você quer sacar? "))
if valor_sacado>saldo:
    print("saldo insuficiente!")
else:
    saldo-=valor_sacado
    print(f"Você sacou {valor_sacado} reais, seu saldo agora é de {saldo} reais.")
#A variável "saldo" muda de valor durante a execução do programa. Para o valor ser alterado, basta atribuirmos outro valor aquela variável.

#Constantes: valores imutáveis, ou seja, não sofre alterações.
#Convenção - declacar tudo em letra maiúscula.
BRAZILIAN_STATES = ["SP", "RJ", "CE"] 