#Métodos da classe list:
import random

lista=[]
#Exemplo: append
for i in random.sample(range(200),k=10):
    lista.append(i) #Adicionar um item em uma lista.
print(lista)

#Exemplo: clear
lista.clear() #Limpar a lista
print(lista)

#Exemplo: count
lista1=[1,1,1,2,2,3,4,5,6,7,7]
print(lista1.count(1)) #Quantas vezes determinado elemento aparece

#Exemplo: extend
linguagens=["Java", "C","Python"]
linguagens2=["C++","C#"]

linguagens.extend(linguagens2) #Juntar listas (exetender)
print(linguagens)

#Exemplo: pop - remover um elemento.(Pilhas L.I.F.O)
linguagens.pop() # C#
linguagens.pop() # C++
item=linguagens.pop(0) # Java
print(item)

#Exemplo: remove - remover um elemnto.
l1=[1,2,3]
l1.remove(1)

#Exemplo: reverse e sort
lista_numeros=[random.randint(1,21) for x in range(10)]

print(f"LISTA NORMAL: {lista_numeros}")

lista_numeros.sort()
print(f"LISTA EM ORDEM CRESCENTE: {lista_numeros}")

lista_numeros.reverse() # Ou sort.(reverse=True) 
print(f"LISTA EM ORDEM DECRESCENTE: {lista_numeros}")

#Exemplo: função len(x)
print(len(lista_numeros)) #Tamanho da lista

