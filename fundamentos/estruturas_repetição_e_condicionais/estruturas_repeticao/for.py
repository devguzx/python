#Comando for: Usado para percorrer um objeto iterável.Faz sentido usar quando sabemos o número de vezes que nosso bloco vai ser executado.

#Exemplo: Quantas vogais tem na string. (string é um objeto iterável)
vogais="aeiou"
palavra=input("Digite uma palavra:").lower()
cont=0
for letra in palavra:
    
    if letra in vogais:
        cont+=1

print(f"Na palavra '{palavra}' existe {cont} vogais.")

#Exemplo: Lista de números 
import random
lista=[x for x in range(1,21)]
print(lista)

#Exemplo: Fatorial
def fatorial(num):
    if num < 0:
        return "Fatorial não definido para negativos."
    fat = 1
    for i in range(1, num + 1):
        fat *= i
    return fat
print(fatorial(6))

#Exemplo: Tabuada de um número
numero=int(input("Digite um número:"))
fim_tabuada=(numero*10)+1
for i in range(0,fim_tabuada,numero):
    print(i,end=" ")
    