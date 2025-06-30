def calcular_dobro(lista):
    for item in lista:
        yield item * 2

array=[10,3,5,6,7,8,]

for i in calcular_dobro(array):
    print(i, end=" ")

