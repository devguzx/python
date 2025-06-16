#Estruturas de dados em python: Lista.

frutas=["laranja", "maçã"]
numeros=list(range(1,11)) #A função list tem que receber um objeto iteravel.
letras=list("devguzx")
print(frutas)
print(numeros)
print(letras)

#Acesso a lista: Os índices começam em 0.
print(frutas[0]) #laranja
print(letras[2]) #v

#Listas Aninhadas: Pode ser usada para fazer arrays bidimensionais (matrizes)
matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in range(3):
    print(matriz[i], end=" ")
    print()

#Iterar listas:
carros=["Gol","Celta", "Palio"]

for carro in carros:
    print(carro, end=", ")
print()
for indice,carro in enumerate(carros): #Função enumerete retorna o índice e o valor correspondente a esse índice.
    print(f"{indice}: {carro}")

#Compressão de listas:
numeros=[1,30,21,2,9,65,34]
pares=[numero for numero in numeros if numero%2==0 ]
print(pares)

quadrados=[num**2 for num in numeros ]
print(quadrados)