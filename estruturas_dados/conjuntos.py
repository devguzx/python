#Estrutura de dados: Set (conjuntos) - Coleção de que não possui objetos repetidos.

print(set([1,2,1,2,1,3,])) #{1,2,3} - Elimina os itens repetidos.

#Acessar dados: Conjuntos não suportam indexação
linguagens={"Python", "Java", "C++"}
linguagens=list(linguagens) #Transformar em lista
print(linguagens[0])

linguagens2={"C#", "JavaScript", "GO"}
for linguagem in linguagens2:
    print(linguagem, end=" - ")
print()

#Métodos da classe set:
conjunto_a={2,3,6,7,8}
conjunto_b={3,4,5,1,3}

print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

conjunto_a.add(25)
print(conjunto_a)
print(len(conjunto_b))
print(1 in conjunto_a) #False