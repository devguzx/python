#Iteradores: é um objeto que pode ser percorrido elemento por elemento, e que implementa os métodos:

#__iter__() -> Retorna o próprio iterador.
#__next__() -> Retorna o próximo item da sequência ou levanta StopIteration quando acaba.

#implementando iterador:
class Contador:
    def __init__(self, maximo):
        self.atual=0
        self.maximo=maximo

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.atual<self.maximo:
            numero=self.atual
            self.atual+=1
            return numero
        else:
            raise StopIteration
        
for num in Contador(10):
    print(num)
