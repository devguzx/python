#Exercício sobre iterador;

class Dobro:
    def __init__(self,lista):
        self.atual=0
        self.lista=lista

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual<len(self.lista):
            dobro=self.lista[self.atual]*2
            self.atual+=1
            return dobro
        else:
            raise StopIteration
        
lista=[3,5,7,9,12]

for item in Dobro(lista):
    print(item)

         